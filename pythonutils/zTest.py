from pythonutils.colors_utils import *
from pythonutils.os_utils import *
from pythonutils.yes_or_no_input import *


def test_colors():
    print("Hi there this is {} and it's nice".format(get_black("_black")))
    print("Hi there this is {} and it's nice".format(get_red("_red")))
    print("Hi there this is {} and it's nice".format(get_yellow("_yellow")))
    print("Hi there this is {} and it's nice".format(get_blue("_blue")))
    print("Hi there this is {} and it's nice".format(get_magenta("_magenta")))
    print("Hi there this is {} and it's nice".format(get_cyan("_cyan")))
    print("Hi there this is {} and it's nice".format(get_white("_white")))
    print("Hi there this is {} and it's nice".format(get_bright_black("_bright_black")))
    print("Hi there this is {} and it's nice".format(get_bright_red("_bright_red")))
    print("Hi there this is {} and it's nice".format(get_bright_green("_bright_green")))
    print("Hi there this is {} and it's nice".format(get_bright_yellow("_bright_yellow")))
    print("Hi there this is {} and it's nice".format(get_bright_black("_black")))
    print("Hi there this is {} and it's nice".format(get_bright_blue("_bright_blue")))
    print("Hi there this is {} and it's nice".format(get_bright_magenta("_bright_magenta")))
    print("Hi there this is {} and it's nice".format(get_bright_cyan("_bright_cyan")))
    print("Hi there this is {} and it's nice".format(get_bright_white("_bright_white")))


def test_get_all_names_in_dir():
    all_names_in_dir = get_all_names_in_dir("/Users/georgekatsaros/Desktop")
    print("\n--Results!--\n")
    for name_in_dir in all_names_in_dir:
        print(name_in_dir)


def test_get_all_in_dir():
    all_in_dir = get_all_in_dir("/Users/georgekatsaros/Desktop")
    print("\n--Results!--\n")
    for in_dir in all_in_dir:
        print(in_dir)


def test_get_all_files_in_dir_sorted_by_size():
    # all_files_in_dir_sorted_by_size = get_all_files_in_dir_sorted_by_size("/Users/georgekatsaros/Desktop", recursive=True)
    # all_files_in_dir_sorted_by_size = get_all_files_in_dir_sorted_by_size("/Users/georgekatsaros/Desktop/Books To Check Out", recursive=True)
    all_files_in_dir_sorted_by_size = get_all_files_in_dir_sorted_by_size("/Users/georgekatsaros/Projects/GlobalGameJam2019", recursive=True)
    print("\n--Results!--\n")
    for path_and_size in all_files_in_dir_sorted_by_size:
        # if ".git" not in path_and_size[0] and "/Build/" not in path_and_size[0] and "Library" not in path_and_size[0]:
        print("{}: {}".format(path_and_size[0], byte_size_to_human_size(path_and_size[1])))


test_get_all_files_in_dir_sorted_by_size()
