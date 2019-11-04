_verbose = False
_fail_log = "Enter the number corresponding to your choice for the below..."


def _multi_choice_input_validation(target, choices):
    if _verbose:
        print(f"_multi_choice_input_validation ( target: {target} , choices: {choices} )")

    if target < 0 or target > len(choices):
        print(_fail_log)
        return False

    return True


def multi_choice_input(prompt, choices):
    if _verbose:
        print(f"multi_choice_input ( prompt: {prompt} , choices: {choices} )")

    options_str = ""
    index = 1
    for choice in choices:
        if len(options_str) > 0:
            options_str = "{}\n".format(options_str)
        options_str = "{}{}: {}".format(options_str, choice, index)
        index += 1

    prompt = "{}\n{}\nYour choice: ".format(prompt, options_str)
    input_multiple_choice = eval(input(prompt))
    print("")
    while _multi_choice_input_validation(input_multiple_choice, choices) is False:
        input_multiple_choice = input(prompt)

    return choices[input_multiple_choice - 1]
