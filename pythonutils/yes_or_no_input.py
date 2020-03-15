from .colors_utils import *
from .str_utils import *

_verbose = False
# regex = re.compile("[^a-zA-Z]")
_fail_log = "You must input y (for yes) or n (for no)!"


def _yes_or_no_validation(target):
    if _verbose:
        print(f"_yes_or_no_validation ( target: {target} )")

    # remove non-letters
    target = regexManager.get(not_letters_pat).sub("", target)

    if len(target) <= 0:
        print(_fail_log)
        return False

    if target[0] == "y":
        return True

    if target[0] == "n":
        return True

    print(_fail_log)
    return False


def yes_or_no(prompt):
    if _verbose:
        print(f"yes_or_no ( target: {prompt} )")

    input_yes_or_no = input("{} y/n: ".format(get_green(prompt)))

    while not _yes_or_no_validation(input_yes_or_no):
        input_yes_or_no = input(get_green("y/n: "))

    input_yes_or_no = regexManager.get(not_letters_pat).sub(input_yes_or_no, "")
    input_yes_or_no = input_yes_or_no.lower()

    if input_yes_or_no[0] == "y":
        return True

    if input_yes_or_no[0] == "n":
        return False

    print("Not sure how you reached this point. Your input was: {}".format(input_yes_or_no))
    return False
