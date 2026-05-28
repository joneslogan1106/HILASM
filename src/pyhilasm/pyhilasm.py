#!/bin/python
import sys

# Global Variables
iota_counter = -1


# Main Functions
def iota(reset=False):
    global iota_counter
    iota_local = iota_counter

    if reset == False:
        iota_local += 1
        iota_counter = iota_local
        return iota_local
    else:
        iota_local = 0
        iota_counter = iota_local
        return iota_counter

# Generic Variables
OP_ADD = iota()
OP_SUB = iota()
OP_MUL = iota(True)


def command_line_utils():
    if sys.argv[1] == "help":
        print("""usage: ./pyhilasm.py [args] program
cx86 - Compiles program according to the x86 ISA""")
        exit(0)
    else:
        print("Not found")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments provided. Try running `help`")
        exit(1)
    else:
        print(f"OP_ADD: {OP_ADD} OP_SUB: {OP_SUB} OP_MUL {OP_MUL}")
        command_line_utils()
