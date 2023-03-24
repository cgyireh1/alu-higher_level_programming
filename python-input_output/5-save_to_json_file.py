#!/usr/bin/python3
"""
Contains function that writes Python obj to file using JSON represenation
"""


def save_to_json_file(my_obj, fname):
    """Writes Python obj to file using JSON represenation
    Args:
        my_obj: python object
        fname: file
    """
    import json

    with open(fname, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
