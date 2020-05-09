import os

_verbose = False


def notify(title, text):
    if _verbose:
        print(f"workbook_search ( title: {title} , text: {text} )")

    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
