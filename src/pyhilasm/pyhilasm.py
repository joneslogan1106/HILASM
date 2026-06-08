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
        iota_local = -1
        iota_counter = iota_local
        return iota_counter

# Generic Variables
OP_ADD    = iota()
OP_SUB    = iota()
OP_MUL    = iota()
OP_DIV    = iota()
OP_PRINT  = iota()
OP_ENDL   = iota()
OP_INT    = iota()

def simulate_program():
    program = [
        ["printa", "add2", "4", "5", "endl"],
        ["printa", "sub2", "10", "9", "endl"],
        ["printa", "mult2", "10", "5", "endl"],
        ["printa", "div2", "500", "10", "endl"]
    ] # At this moment, currently hardcoded
    keywords = ["printa", "add"]


    ast = [] # Program as pure numeric values
    numbered_program = []
    for line in program:
        for bit in line:
            if bit == "printa":
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["PRINT", OP_PRINT, 0]
                })
            elif bit[:-1] == "add":
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["ADD", OP_ADD, int(bit[3:])]
                })
            elif bit[:-1] == "sub":
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["SUB", OP_SUB, int(bit[3:])]
                })
            elif bit[:-1] == "mult":
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["MUL", OP_MUL, int(bit[4:])]
                })
            elif bit[:-1] == "div":
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["DIV", OP_DIV, int(bit[3:])]
                })
            elif bit == "endl":
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["ENDL", OP_ENDL]
                })
            elif isinstance(int(bit), int):
                ast.append({
                    'program_line': program.index(line) + 1,
                    'operand': ["INT", OP_INT, int(bit)]
                })

    #flags, helps the program know whats happenning
    print_arithmetic_flag = False
    add_flag = [False, 0]
    makeshift_stack = []
    for i in range(len(ast)-1):
        if ast[i]['operand'][1] == OP_PRINT:
            if ast[i]['operand'][2] == 0: # This means we are printing the result of an arithmetic operation
                print_arithmetic_flag = True
        elif ast[i]['operand'][1] == OP_ADD:
            add_flag = [True, ast[i]['operand'][2]]
        elif ast[i]['operand'][1] == OP_INT:
            makeshift_stack.append(ast[i]['operand'][2])
        elif print_arithmetic_flag == True and len(makeshift_stack) == add_flag[1] and len(makeshift_stack) >= 2:
            y = makeshift_stack.pop()
            x = makeshift_stack.pop()
            print(x+y)
            print_arithmetic_flag = False
            add_flag = [False, 0]
            makeshift_stack =[]
        elif ast[i]['operand'][1] == OP_ENDL: # DO NOT REMOVE THISTATEMENT
            print_arithmetic_flag = False
            add_flag = [False, 0]
            makeshift_stack = []
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
