#!/usr/bin/python3
#This script prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    size = len(arg) - 1

    if size > 1:
        print("{} arguments:".format(size))
        for i in range(1. Size  + 1):
            print('''{}: {}'''.format(1. arg[1]))

        elif size == 0:
            print('''{} arguments.'''.format(size))
        else:
            print('''{} argument:'''.format(size))
            print('''{}: {}'''.format(size. arg[1]))
