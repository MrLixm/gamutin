import ast
import json
import os
import logging
import re
import sys
from pathlib import Path
from typing import Optional

import click
import colour
import numpy

import gamutin.core.gamut
import gamutin.core.colorspaces
import gamutin.core.io
from gamutin.core.exceptions import raisePathExists

logger = logging.getLogger(__name__)


def launch_gui(source_file: Path = None):
    """
    Create and open the interface by showing the main window.
    """

    logger.debug(f"[launch_gui] Started. Importing <gamutin.editor> ...")
    # defer import of the editor package only if the user ask to open the GUI
    import gamutin.editor

    app = gamutin.editor.getQApp()
    logger.debug(f"[launch_gui] {app=}")

    main_window = gamutin.editor.MainWindow()
    main_window.show()
    # TODO set sourcefile on mainWindow

    if app:
        sys.exit(app.exec_())


@click.group(invoke_without_command=True)
@click.version_option("{}".format(gamutin.__version__))
@click.option(
    "--debug",
    is_flag=True,
    envvar=gamutin.c.Env.logs_debug.value,
    help="This will enable the debug mode which display more informations and disable some features.",
    # --debug is used via sys.argv across the app, do not remove.
)
def cli(debug: bool):
    """
    Analyze the input image to see how it fits in the pointer's gamut.

    Opens the GUI by not providing any argument.
    """
    logger.debug(f"[cli] Started.(cwd={os.getcwd()})[{debug=}]")

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and "--debug" in sys.argv):
        launch_gui()

    return


@cli.command()
@click.argument("source_file", type=click.Path(exists=True), required=False)
def gui(source_file: str):
    """
    Specifically ask to launch the GUI with the given configuration.

    SOURCE_FILE: path to an existing image file
    """
    source_file = Path(source_file)
    launch_gui(source_file=source_file)


@cli.command()
@click.argument("source_file", type=click.Path(exists=True))
@click.argument("target_file", type=click.Path(file_okay=True))
@click.option(
    "--mask_file",
    type=click.Path(exists=True),
    help=(
        "File path to mask in the [0-1] range to specify which pixel need to be processed. "
        "Interpeeted as scalar data."
    ),
)
@click.option(
    "--use_alpha_as_mask",
    is_flag=True,
    default=False,
    help="If true use the alpha channel to specify which pixel need to be processed.",
)
@click.option(
    "--colorspace",
    required=True,
    type=str,
    default="sRGB:linear",
    help="Colorspace encoding of the source_file. See `colorspaces` command for a list of availables options.",
)
@click.option(
    "--ref_colorspace",
    required=True,
    type=str,
    default=gamutin.core.colorspaces.POINTER_GAMUT_COLORSPACE.name,
    help="Colorspace to use the gamut as limit for comparing the input.",
)
@click.option(
    "--blend_mode",
    type=str,
    default=gamutin.core.gamut.CompositeBlendModes.over.name,
    help="How to blend the out of gamut map with the original image. See `blendmodes` command for a list of availables options.",
)
@click.option(
    "--target_colorspace",
    type=str,
    help=(
        "Colorspace encoding of the target_file. "
        "See `colorspaces` command for a list of availables options."
        "If not specified, the colorspace for the source will be used."
    ),
)
@click.option(
    "--invalid_color",
    default="(1, 0, 0)",
    help=(
        "Color to use for out of pointer's gamut values. "
        "Must be a tuple of 3 floats as (R,G,B). "
        "The value is assumed to be encoded in the same colorspace as SOURCE_FILE."
    ),
)
@click.option(
    "--valid_color",
    default="(0, 0, 0)",
    help=(
        "Color to use for values inside of pointer's gamut. "
        "Must be a tuple of 3 floats as (R,G,B). "
        "The value is assumed to be encoded in the same colorspace as SOURCE_FILE."
    ),
)
@click.option(
    "--tolerance",
    default=0.0,
    help="How far from the pointer gamut you authorize the pixel values to be.[default=0] ex: 0.1",
)
@click.option("--subimage", default=0, help="Subimage index to use on SOURCE_FILE")
@click.option("--mipmap", default=0, help="Mipmap index to use on SOURCE_FILE")
def check(
    source_file: str,
    target_file: str,
    mask_file: str,
    use_alpha_as_mask: bool,
    blend_mode: str,
    colorspace: str,
    ref_colorspace: str,
    target_colorspace: Optional[str],
    tolerance: float,
    invalid_color: str,
    valid_color: str,
    subimage,
    mipmap,
):
    """
    Check given image is inside the pointer's gamut.

    Produce a new image ``target_file`` with values of ``source_file`` that are outside the pointer's gamut.

    SOURCE_FILE: path to an existing image file. Format must be supported by OIIO

    TARGET_FILE: file path to write the image. Relative path to the SOURCE_FILE supported.

    (colorspace conversions use Bradford as CAT)
    """
    logger.debug(
        "[check] called with"
        + json.dumps(
            click.get_current_context().params, indent=4, default=str, sort_keys=True
        )
    )
    source_file = Path(source_file)
    target_file = Path(target_file)
    if not target_file.is_absolute():
        target_file = source_file.parent / target_file
        target_file = target_file.resolve().absolute()
    if mask_file:
        mask_file: Optional[Path] = Path(mask_file)

    if mask_file and use_alpha_as_mask:
        raise ValueError('You can\'t specify "use_alpha_as_mask" and "mask_file"')

    for color_arg in [invalid_color, valid_color]:
        if not color_arg.startswith("(") or not color_arg.endswith(")"):
            raise ValueError(
                f'Argument "{color_arg}" passed must be wrapped around parenthesis.'
            )
        if not re.match(r"\(\s*\d.+\d\)", color_arg):
            raise ValueError(
                f'Argument "{color_arg}" passed must start AND end by an digit after/before the parenthesis.'
            )

    invalid_color: tuple[float, float, float] = ast.literal_eval(invalid_color)
    valid_color: tuple[float, float, float] = ast.literal_eval(valid_color)

    _colorspace = gamutin.core.colorspaces.get_colorspace(colorspace)
    _ref_colorspace = gamutin.core.colorspaces.get_colorspace(ref_colorspace)
    _target_colorspace = target_colorspace or colorspace
    _target_colorspace = gamutin.core.colorspaces.get_colorspace(_target_colorspace)

    for _given_colorspace, _resolved_colorspace in zip(
        (colorspace, ref_colorspace, target_colorspace),
        (_colorspace, _ref_colorspace, _target_colorspace),
    ):

        if not _resolved_colorspace:
            raise ValueError(
                f'Given colorspace "{_given_colorspace}" is not recognized. '
                f"Must be one of {gamutin.core.colorspaces.get_available_colorspaces_names()}"
            )

    del _given_colorspace, _resolved_colorspace

    if _colorspace == gamutin.core.colorspaces.POINTER_GAMUT_COLORSPACE:
        raise ValueError(
            f"You can't use the {gamutin.core.colorspaces.POINTER_GAMUT_COLORSPACE.name} colorspace as source colorspace !"
        )
    if _target_colorspace == gamutin.core.colorspaces.POINTER_GAMUT_COLORSPACE:
        raise ValueError(
            f"You can't use the {gamutin.core.colorspaces.POINTER_GAMUT_COLORSPACE.name} colorspace as target colorspace !"
        )

    _blend_mode = gamutin.core.gamut.CompositeBlendModes[blend_mode]

    _mask_used = bool(mask_file or use_alpha_as_mask)

    logger.info(
        f"[check] Started processing {source_file=}({subimage=}:{mipmap=}) --> {target_file=} X {_mask_used=}\n"
        f"  with {_colorspace.name=}, {_target_colorspace.name=}, {tolerance=}, {blend_mode=}"
    )

    input_image = gamutin.core.io.ImageRead(path=source_file, colorspace=_colorspace)
    input_array = input_image.read_array(
        channels=("R", "G", "B"),
        subimage=subimage,
        mipmap=mipmap,
    )

    mask_array: Optional[numpy.ndarray] = None
    if mask_file:
        mask_image = gamutin.core.io.ImageRead(path=mask_file, colorspace=None)
        mask_array = mask_image.read_array(channels=("R",))

        if mask_array.shape[:-1] != input_array.shape[:-1]:
            raise ValueError(
                f"Given mask file {mask_file} doesn't have the same dimensions as the input_file: "
                f"{mask_array.shape=} != {input_array.shape=}"
            )
    elif use_alpha_as_mask:
        mask_array = input_image.read_array(channels=("A",))
        if not numpy.any(mask_array):
            raise ValueError(
                '"use_alpha_as_mask" specified but the alpha channel seems empty (only zeros).'
            )

    # convert single channel to "R-G-B"
    if mask_array is not None and mask_array.shape[-1] == 1:
        mask_array = mask_array[:, :, 0]
        mask_array = numpy.stack((mask_array,) * 3, axis=-1)

    logger.debug("[check] calling transform_out_of_pg_values...")
    result_array = gamutin.core.gamut.transform_out_of_gamut_values(
        input_array=input_array,
        input_colorspace=_colorspace,
        reference_colorspace=_ref_colorspace,
        invalid_color=invalid_color,
        valid_color=valid_color,
        tolerance_amount=tolerance,
        blend_mode=_blend_mode,
        chromatic_adaptation_transform=gamutin.core.colorspaces.ChromaticAdaptationTransform.default,
        mask=mask_array,
    )

    output_array = gamutin.core.colorspaces.colorspace_to_colorspace(
        result_array,
        _colorspace,
        _target_colorspace,
        chromatic_adaptation_transform=gamutin.core.colorspaces.ChromaticAdaptationTransform.default,
    )

    output_image = gamutin.core.io.ImageWrite(
        target_file, colorspace=_target_colorspace
    )
    output_image.set_pixels(output_array)
    output_image.write()

    raisePathExists(target_file)
    logger.info(f"[check] Finished writing <{target_file}>.")
    return


@cli.command()
def colorspaces():
    """
    List all colorspaces availables.
    """
    colorspace_names_list = (
        gamutin.core.colorspaces.get_available_colorspaces_names_aliases()
    )
    out_str = ""
    for colorspace_aliases in colorspace_names_list:
        aliases = '", "'.join(colorspace_aliases[1:])
        out_str += f'{colorspace_aliases[0]: <30} - aliases: "{aliases}"\n'

    out_str += '\nYou can ask a "linear" variant of the colorspace (== no transfer function) by adding ":linear" at the end of the colorspace name.'
    click.echo(out_str)


@cli.command()
def blendmodes():
    """
    List all blending modes availables.
    """
    blend_mode_list = gamutin.core.gamut.CompositeBlendModes.__all__()
    blend_mode_list = [bm.name for bm in blend_mode_list]
    click.echo(blend_mode_list)


@cli.command()
@click.argument("source_file", type=click.Path(exists=True))
@click.option(
    "--verbose",
    is_flag=True,
    default=False,
    help="Display as much informations as possible.",
)
def imageinfo(source_file: str, verbose: bool):
    """
    Display useful information about the given file
    """
    source_file = Path(source_file)
    image = gamutin.core.io.ImageRead(path=source_file, colorspace=None)
    image_repr = gamutin.core.io.ImageRepr(image=image)

    if verbose:
        data_dict = image_repr.full_dict
    else:
        data_dict = image_repr.simple_dict

    out_str = json.dumps(
        data_dict,
        indent=4,
        sort_keys=True,
        separators=("", " : "),
    )
    out_str = out_str.replace("{", "").replace("}", "")
    click.echo(out_str)
