import os

_verbose = False


def get_all_names_in_dir(target_dir):
    if _verbose:
        print(f"get_all_names_in_dir ( target_dir: {target_dir} )")

    return os.listdir(target_dir)


def get_all_in_dir(target_dir, full_path=True, recursive=False, include_dirs=True, include_files=True):
    if _verbose:
        print(f"get_all_paths_in_dir ( target_dir: {target_dir} , full_path: {full_path} , "
              f"recursive: {recursive}, include_dirs: {include_dirs} , include_files: {include_files} )")

    if not include_dirs and not include_files:
        raise Exception("What are you looking for with include_dirs and include_files set to false?!")

    get_all_paths_in_dir_result = []
    for (target_dir, dir_names, file_names) in os.walk(target_dir):
        # update all results to their full path
        if full_path:
            if include_dirs:
                i = 0
                for dir_name in dir_names:
                    dir_names[i] = os.path.abspath(os.path.join(target_dir, dir_name))
                    i += 1
            if include_files:
                i = 0
                for file_name in file_names:
                    file_names[i] = os.path.abspath(os.path.join(target_dir, file_name))
                    i += 1

        if include_dirs:
            get_all_paths_in_dir_result.extend(dir_names)
        if include_files:
            get_all_paths_in_dir_result.extend(file_names)

        if not recursive:
            break

    return get_all_paths_in_dir_result


# returns list of tuples sorted from least to greatest
def get_all_files_in_dir_sorted_by_size(target_dir, recursive=False):
    if _verbose:
        print(f"get_all_files_in_dir_sorted_by_size ( target_dir: {target_dir} , recursive: {recursive} )")

    get_all_files_in_dir_sorted_by_size_results = []

    file_paths = get_all_in_dir(target_dir, include_dirs=False, recursive=recursive)
    for file_path in file_paths:
        # for some reason this breaks on system links
        if not os.path.islink(file_path):
            get_all_files_in_dir_sorted_by_size_results.append((file_path, os.path.getsize(file_path)))

    get_all_files_in_dir_sorted_by_size_results.sort(key=lambda x: x[1])

    return get_all_files_in_dir_sorted_by_size_results


def get_desktop_dir_path():
    if _verbose:
        print("get_desktop_dir_path")
    return os.path.expanduser("~/Desktop/")


def ensure_file_path_exists(file_path):
    if _verbose:
        print(f"ensure_file_path_exists ( file_path: {file_path} )")

    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass


def get_file_name_from_path(path, with_extension=False):
    if _verbose:
        print(f"extract_file_name_from_path ( path: {path} , with_extension: {with_extension} )")

    return os.path.basename(path) if with_extension else os.path.splitext(os.path.basename(path))[0]


def get_parent_dir(target_path, amount=1):
    debug = f"get_parent_dir ( target_file: {target_path} , amount: {amount} )"
    if _verbose:
        print(debug)

    if amount < 0:
        print(f"{debug} | amount can't be less than zero, setting it to 1")
        amount = 1

    parent_dir = "Not found"

    i = 0
    while i < amount:
        i += 1
        target_path = os.path.join(target_path, os.pardir)
        parent_dir = os.path.abspath(target_path)

    return parent_dir


def ensure_dir_path_exists(path):
    if _verbose:
        print(f"ensure_dir_path_exists ( path: {path} )")

    if os.path.isfile(path):
        path = os.path.dirname(path)

    if not os.path.exists(path):
        os.makedirs(path)
        if _verbose:
            print(f"ensure_dir_path_exists ( path: {path} ) | created dir path since it did not exist!")


def make_unique_time_folder_at_path(path):
    if _verbose:
        print("make_unique_time_folder_at_path ( path: {} )".format(path))
        print(str(datetime.datetime.now()))

    new_path = os.path.join(path, str(datetime.datetime.now()))
    ensure_dir_path_exists(new_path)

    return new_path
