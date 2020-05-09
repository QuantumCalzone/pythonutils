import ctypes
import os

_verbose = False


def is_hidden(path):
    if _verbose:
        print(f"is_hidden ( path: {path} )")

    name = os.path.basename(os.path.abspath(path))
    return name.startswith('.') or has_hidden_attribute(path)


def has_hidden_attribute(path):
    if _verbose:
        print(f"has_hidden_attribute ( path: {path} )")

    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(path))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False

    return result
