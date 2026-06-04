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
OP_ADD    = iota()
OP_SUB    = iota()
OP_MUL    = iota()
OP_DIV    = iota()
OP_PRINT  = iota()
OP_ENDL   = iota()
OP_NUM    = iota()

def simulate_program():
    program = [
        ["printa", "add2", "4", "5", "endl"],
        ["printa", "sub2", "10", "9", "endl"],
        ["printa", "mult2", "10", "5", "endl"],
        ["printa", "div2", "500", "10", "endl"]
    ] # At this moment, currently hardcoded
    keywords = ["printa", "add"]


    numbered_program = [] # Program as pure numeric values
    for line in program:
        for bit in line:
            if bit == "printa":
                numbered_program.append([program.index(line) + 1, [OP_PRINT, 0]]) # says program line, print operation, with arithmetic funvtion
            elif bit[:-1] == "add":
                numbered_program.append([program.index(line) + 1, [OP_ADD, int(bit[3:])]]) # says program line, adding operation, then ading the information that there are x numbers being added
            elif bit[:-1] == "sub":
                numbered_program.append([program.index(line) + 1, [OP_SUB, int(bit[3:])]]) # says program line, subtrction operation, with x arguments
            elif bit[:-1] == "mult":
                numbered_program.append([program.index(line) + 1, [OP_MUL, int(bit[4:])]]) # says program line, multiiply , x numbers
            elif bit[:-1] == "div":
                numbered_program.append([program.index(line) + 1, [OP_DIV, int(bit[3:])]])
            elif bit == "endl":
                numbered_program.append([program.index(line) + 1, OP_ENDL]) # js says its the end of the line
            elif isinstance(int(bit), int):
                numbered_program.append([program.index(line) + 1, [OP_NUM, int(bit)]]) # says program line, its a number, then what that number is
        print(numbered_program)
# Basic command line styuff
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
