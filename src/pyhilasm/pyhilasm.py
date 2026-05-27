#!/bin/python
import sys


def command_line_utils():
    if sys.argv[1] == "help":
        print("""usage: ./pyhilasm.py [args] program
cx86 - Compiles program according to the x86 ISA""")
        exit(0)
    else:
        print("Not implemented/Not found")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments provided. Try running `help`")
        exit(1)
    else:
        command_line_utils()
