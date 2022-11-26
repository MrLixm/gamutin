import os
import logging
import sys

import click

import pgcheck

__all__ = ("cli",)
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
        launch_gui()

    return


def launch_gui():
    """
    Launch the interface and the QApp if there is none active.
    """
    logger.debug(f"[launch_gui] Started. Importing <pgcheck.editor> ...")
    # defer import of the editor package only if the user ask to open the GUI
    import pgcheck.editor

    app = pgcheck.editor.getQApp()
    logger.debug(f"[launch_gui] {app=}")

    main_window = pgcheck.editor.MainWindow()
    main_window.show()

    if app:
        sys.exit(app.exec_())
