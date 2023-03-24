#!/usr/bin/python3
"""
Contains function that writes to text file and returns num chars written
"""


def write_file(fname="", text=""):
    """writes to text file and returns num chars written"""
    with open(fname, mode="w", encoding="utf-8") as f:
        return(f.write(text))
