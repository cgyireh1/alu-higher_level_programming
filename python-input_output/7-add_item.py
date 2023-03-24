#!/usr/bin/python3
"""
Contains function that adds and saves to Python obj to JSON file; loads objects
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

fname = "add_item.json"

try:
    existing_content = load_from_json_file(fname)
except FileNotFoundError:
    existing_content = []

save_to_json_file(existing_content + argv[1:], fname)
