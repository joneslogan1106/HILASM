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
OP_ADD   = iota()
OP_SUB   = iota()
OP_MUL   = iota()
OP_DIV   = iota()
OP_PRINT = iota()

def simulate_program():
    program = [
        ["add", "4", "5", "print"],
        ["sub 10 9 print"],
        ["mult 10 5 print"],
        ["div 500 10 print"]
    ]

    for i in


def command_line_utils():
    if sys.argv[1] == "help":
        print("""usage: ./pyhilasm.py program_file [args]
sim - Simulates a program file
cx86 - Compiles program according to the x86 ISA""")
        exit(0)
    elif sys.argv[1] == "sim":
        simulate_program()
    elif sys.argv[1] == "cx86":
        assert False, "Not implemented"
    else:
        print("Not found")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments provided. Try running `help`")
        exit(1)
    else:
        command_line_utils()
