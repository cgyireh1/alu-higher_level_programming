#!/usr/bin/python3
"""
Contains class MyList
inherits from list
Has public instance method to print sorted
"""


class MyList(list):
    """inherits from list
    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of ints sorted in ascending order"""
        print(sorted(self))
