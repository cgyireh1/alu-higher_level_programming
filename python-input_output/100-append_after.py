#!/usr/bin/python3
"""
Contains a function that inserts a line of text to a file.
"""

def append_after(fname="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after
    each line containing a specific string.
    """
    out = ""
    with open(fname, 'r') as f:
        for line in f:
            out += line
            if search_string in line:
                out += new_string

    with open(fname, 'w') as f:
        f.write(out)
