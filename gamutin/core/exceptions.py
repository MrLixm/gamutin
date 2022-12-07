from pathlib import Path


def raisePathExists(path: Path) -> None:
    """
    Raises:
        FileNotFoundError: if the passed path doesn't exist on disk.
    """
    if not path.exists():
        if path.parent.exists() and path.parent.is_file():
            raise FileNotFoundError(f"{path=}\nparent is a file !")
        raise FileNotFoundError(f"{path=}\n{path.parent.exists()=}")
