import re


class RegexManager:
    _regexes = {}

    def get(self, pattern):
        if _verbose:
            print(f"get ( pattern: {pattern} )")

        if pattern not in self._regexes:
            self._regexes[pattern] = re.compile(pattern)

        return self._regexes[pattern]


# def byte_size_to_human_size(byte_size, suffix="B"):
#     if _verbose:
#         print(f"byte_size_to_human_size ( byte_size: {byte_size} , suffix: {suffix} )")
#
#     for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
#         if abs(byte_size) < 1024.0:
#             return "%3.1f%s%s" % (byte_size, unit, byte_size)
#
#         byte_size /= 1024.0
#
#     return "%.1f%s%s" % (byte_size, 'Yi', suffix)

def byte_size_to_human_size(byte_size, do_round=True):
    if _verbose:
        print(f"byte_size_to_human_size ( byte_size: {byte_size} , do_round: {do_round} )")

    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    power_labels = {0: "", 1: "kilo", 2: "mega", 3: "giga", 4: "tera"}

    while byte_size > power:
        byte_size /= power
        n += 1

    return (round(byte_size) if do_round else byte_size), power_labels[n] + "bytes"



_verbose = False
regexManager = RegexManager()
before_first_comma_pat= r"^([^,])+"
after_first_comma_and_space_pat = r"(?<=\, ).*"
only_numbers_pat = r"[^a-z ]\ *([.0-9])*\d"
not_letters_pat = r"[^a-zA-Z]"
number_groups_pat = r"[0-9]+"
email_validator_pat = r"/\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b/gi"
