"""
Convert an image to a .ico to use with Qt.
"""
from pathlib import Path
import PIL.Image

import gamutin.editor

sources = (gamutin.editor.cfg.resources.get_icon("logo-main.png"),)
targets = (gamutin.editor.cfg.resources.icon_main,)


def pathToIco(source_path: Path, target_path: Path):
    assert str(target_path).endswith(".ico"), f"{target_path} is not a .ico file."
    source_path = source_path.resolve()
    target_path = target_path.resolve()

    image = PIL.Image.open(source_path)
    image.save(
        target_path,
        sizes=[
            (16, 16),
            (24, 24),
            (32, 32),
            (48, 48),
            (64, 64),
            (128, 128),
            (256, 256),
        ],
        bitmap_format="png",
    )

    print(f"[ico_builder][pathToIco] Finished: {source_path} -> {target_path}")
    return


def run():
    print(f"[ico_builder][run] Started processing {len(sources)} images")

    for source, target in zip(sources, targets):
        pathToIco(source, target)

    print("[ico_builder][run] Finished.")
    return


if __name__ == "__main__":
    run()
