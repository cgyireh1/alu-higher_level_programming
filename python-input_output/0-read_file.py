#!/usr/bin/python3
"""
Contains function that reads and prints contents from file
"""


def read_file(fname=""):
    """Read and print text from file"""
    with open(fname, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
