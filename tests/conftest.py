import pytest
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture
def imagepath_wheel_mpart():
    return DATA_DIR / "wheel_mpart.exr"


@pytest.fixture
def imagepath_color_bars_alpha():
    return DATA_DIR / "color_bars_alpha.tif"


@pytest.fixture
def imagepath_wheel_mchannel():
    return DATA_DIR / "wheel_mchannel.exr"
