from colors_utils import *

_verbose = False


def stripped_input(prompt):
    if _verbose:
        print(f"stripped_input ( prompt: {prompt} )")
    val = input(get_green(prompt))
    val = val.strip()
    return val
