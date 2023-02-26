from gamutin.core import io


def test_get_extensions_for_supported_formats():
    extensions = io.c.get_extensions_for_supported_formats(["jpeg"])
    assert extensions == [".jpg", ".jpe", ".jpeg", ".jif", ".jfif", ".jfi"]

    extensions = io.c.get_extensions_for_supported_formats(["openexr", "png"])
    assert extensions == [".exr", ".sxr", ".mxr", ".png"]
