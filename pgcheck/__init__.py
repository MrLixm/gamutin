# initialization of the package
from . import c
from .c import __version__
from . import cfg

# and then we do not import anything else to avoid bloating the namespace
# as the user might not use all the sub-packages.
# He will have to manually `import pgcheck.editor` , ...


def debug():
    """
    Log debug messages for the ``c`` and ``cfg`` module.
    """
    c.__debugthis__()
    cfg.__debugthis__()
    return
