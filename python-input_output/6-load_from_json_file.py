#!/usr/bin/python3
"""
Contains function that creates a Python obj from JSON file
"""


def load_from_json_file(fname):
    """Creates a Python obj from JSON file
    Args:
        fname: file
    """
    import json

    with open(fname, mode="r", encoding="utf-8") as f:
        return json.load(f)
