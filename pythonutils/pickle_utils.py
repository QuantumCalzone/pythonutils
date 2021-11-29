import os
import pickle

_verbose = False


def load_pickle(path, create_if_non_existent=None):
    log = f"load_pickle ( path: {path} , create_if_non_existent: {create_if_non_existent is not None} )"
    if _verbose:
        print(log)

    if not os.path.exists(path):
        print(f"{log} | Could not find pickle!")
        if create_if_non_existent is not None:
            save_pickle(create_if_non_existent, path)
        return create_if_non_existent

    pickle_file = open(path, "rb")
    data = pickle.load(pickle_file)
    pickle_file.close()

    return data


def save_pickle(data, path):
    if _verbose:
        print(f"save_pickle_dictionary ( data: {data} , path: {path} )")

    with open(path, "wb") as f:
        pickle.dump(data, f)
