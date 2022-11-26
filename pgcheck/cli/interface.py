import os
import logging
import sys

import click

import pgcheck

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
    TODO write a small description of the app
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
    default="sRGB",
    help="Colorspace encoding of the source_file. See `colorspaces` command for a list of availables options.",
)
@click.option(
    "--invalid_color",
    default="(1, 0, 0)",
    help=(
        "Color to use for out of pointer's gamut values. "
        "Must be a tuple of 3 floats as (R,G,B). "
        "The value while be directly encoded in TARGET_FILE."
    ),
)
@click.option(
    "--valid_color",
    default="(0, 0, 0)",
    help=(
        "Color to use for values inside of pointer's gamut. "
        "Must be a tuple of 3 floats as (R,G,B). "
        "The value while be directly encoded in TARGET_FILE."
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
    colorspace,
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
    """
    pass


@cli.command()
def colorspaces():
    """
    List all colorspaces availables.
    """
    pass
