_verbose = False

_black = "\033[30m"
_red = "\033[31m"
_green = "\033[32m"
_yellow = "\033[33m"
_blue = "\033[34m"
_magenta = "\033[35m"
_cyan = "\033[36m"
_white = "\033[37m"
_bright_black = "\033[90m"
_bright_red = "\033[91m"
_bright_green = "\033[92m"
_bright_yellow = "\033[93m"
_bright_blue = "\033[94m"
_bright_magenta = "\033[95m"
_bright_cyan = "\033[96m"
_bright_white = "\033[97m"


def _get_colored(val, color):
    if _verbose:
        print(f"_get_colored ( val: {val} , color: {color} )")
    return f"{color}{val}{_white}"


def get_black(val):
    if _verbose:
        print(f"get_black ( val: {val} )")
    return _get_colored(val, _black)


def get_red(val):
    if _verbose:
        print(f"get_red( val: {val} )")
    return _get_colored(val, _red)


def get_green(val):
    if _verbose:
        print(f"get_green( val: {val} )")
    return _get_colored(val, _green)


def get_yellow(val):
    if _verbose:
        print(f"get_yellow( val: {val} )")
    return _get_colored(val, _yellow)


def get_blue(val):
    if _verbose:
        print(f"get_blue( val: {val} )")
    return _get_colored(val, _blue)


def get_magenta(val):
    if _verbose:
        print(f"get_magenta( val: {val} )")
    return _get_colored(val, _magenta)


def get_cyan(val):
    if _verbose:
        print(f"get_cyan( val: {val} )")
    return _get_colored(val, _cyan)


def get_white(val):
    if _verbose:
        print(f"get_white( val: {val} )")
    return _get_colored(val, _white)


def get_bright_black(val):
    if _verbose:
        print(f"get_bright_black( val: {val} )")
    return _get_colored(val, _bright_black)


def get_bright_red(val):
    if _verbose:
        print(f"get_bright_red( val: {val} )")
    return _get_colored(val, _bright_red)


def get_bright_green(val):
    if _verbose:
        print(f"get_bright_green( val: {val} )")
    return _get_colored(val, _bright_green)


def get_bright_yellow(val):
    if _verbose:
        print(f"get_bright_yellow( val: {val} )")
    return _get_colored(val, _bright_yellow)


def get_bright_blue(val):
    if _verbose:
        print(f"get_bright_blue( val: {val} )")
    return _get_colored(val, _bright_blue)


def get_bright_magenta(val):
    if _verbose:
        print(f"get_bright_magenta( val: {val} )")
    return _get_colored(val, _bright_magenta)


def get_bright_cyan(val):
    if _verbose:
        print(f"get_bright_cyan( val: {val} )")
    return _get_colored(val, _bright_cyan)


def get_bright_white(val):
    if _verbose:
        print(f"get_bright_white( val: {val} )")
    return _get_colored(val, _bright_white)

