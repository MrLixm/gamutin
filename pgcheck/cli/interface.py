import ast
import os
import logging
import re
import sys
from pathlib import Path
from typing import Optional

import click
import colour

import pgcheck.core.pointergamut
import pgcheck.core.colorspaces
import pgcheck.core.io
from pgcheck.core.exceptions import raisePathExists

logger = logging.getLogger(__name__)


@click.group(invoke_without_command=True)
@click.version_option("{}".format(pgcheck.__version__))
@click.option(
    "--debug",
    is_flag=True,
    envvar=pgcheck.c.Env.logs_debug.value,
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
        gui()

    return


@cli.command()
@click.argument("source_file", type=click.Path(exists=True), required=False)
def gui(source_file):
    """
    Specifically ask to launch the GUI with the given configuration.

    SOURCE_FILE: path to an existing image file
    """
    logger.debug(f"[launch_gui] Started. Importing <pgcheck.editor> ...")
    # defer import of the editor package only if the user ask to open the GUI
    import pgcheck.editor

    app = pgcheck.editor.getQApp()
    logger.debug(f"[launch_gui] {app=}")

    main_window = pgcheck.editor.MainWindow()
    main_window.show()
    # TODO set sourcefile on mainWindow

    if app:
        sys.exit(app.exec_())


@cli.command()
@click.argument("source_file", type=click.Path(exists=True))
@click.argument("target_file", type=click.Path(file_okay=True))
@click.option(
    "--colorspace",
    required=True,
    type=str,
    default="sRGB Linear",
    help="Colorspace encoding of the source_file. See `colorspaces` command for a list of availables options.",
)
@click.option(
    "--blend_mode",
    type=str,
    default=pgcheck.core.pointergamut.CompositeBlendModes.over.name,
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
    source_file,
    target_file,
    blend_mode: str,
    colorspace: str,
    target_colorspace: Optional[str],
    tolerance: float,
    invalid_color: str,
    valid_color: str,
    subimage,
    mipmap,
):
    """
    Produce a new image ``target_file`` with values of ``source_file`` that are outside the pointer's gamut.

    SOURCE_FILE: path to an existing image file. Format must be supported by OIIO

    TARGET_FILE: file path to write the image. Relative path to the SOURCE_FILE supported.

    (colorspace conversions use Bradford as CAT)
    """
    source_file = Path(source_file)
    target_file = Path(target_file)
    if not target_file.is_absolute():
        target_file = source_file.parent / target_file
        target_file = target_file.resolve().absolute()

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

    _colorspace = pgcheck.core.colorspaces.get_colorspace(colorspace)
    if not _colorspace:
        raise ValueError(
            f'Given colorspace "{colorspace}" is not recognized. '
            f"Must be one of {pgcheck.core.colorspaces.get_available_colorspaces_names()}"
        )

    _target_colorspace = target_colorspace or colorspace
    _target_colorspace = pgcheck.core.colorspaces.get_colorspace(colorspace)
    if not _target_colorspace:
        raise ValueError(
            f'Given target colorspace "{target_colorspace}" is not recognized. '
            f"Must be one of {pgcheck.core.colorspaces.get_available_colorspaces_names()}"
        )

    _blend_mode = pgcheck.core.pointergamut.CompositeBlendModes[blend_mode]

    logger.info(
        f"[check] Started processing {source_file=}({subimage=}{mipmap=}), {target_file=} "
        f"with {colorspace=}, {target_colorspace=}, {tolerance=}, {blend_mode=}"
    )

    input_image = pgcheck.core.io.ImageRead(path=source_file, colorspace=_colorspace)
    input_array = input_image.read_array(subimage, mipmap)

    result_array = pgcheck.core.pointergamut.transform_out_of_pg_values(
        input_array=input_array,
        input_colorspace=_colorspace,
        invalid_color=invalid_color,
        valid_color=valid_color,
        tolerance_amount=tolerance,
        blend_mode=_blend_mode,
    )

    output_array = colour.RGB_to_RGB(
        result_array,
        _colorspace,
        _target_colorspace,
        chromatic_adaptation_transform="Bradford",
        apply_cctf_decoding=True,
        apply_cctf_encoding=True,
    )

    output_image = pgcheck.core.io.ImageWrite(
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
    colorspace_list = pgcheck.core.colorspaces.get_available_colorspaces_names()
    click.echo(",\n".join(colorspace_list))


@cli.command()
def blendmodes():
    """
    List all blending modes availables.
    """
    blend_mode_list = pgcheck.core.pointergamut.CompositeBlendModes.__all__()
    blend_mode_list = [bm.name for bm in blend_mode_list]
    click.echo(blend_mode_list)
