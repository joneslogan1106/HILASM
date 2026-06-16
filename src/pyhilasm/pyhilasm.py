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
        ["printa", "div2", "500", "10", "endl"],
        ["printa", "sub3", "5", "9", "3", "endl"],
        ["printa", "add3", "2", "5", "8", "endl"],
        ["printa", "mult3", "59", "9", "38", "endl"],
        ["printa", "div3", "500", "10", "2", "endl"]
    ] # At this moment, currently hardcoded


    ast = [] # Program as pure numeric values
    numbered_program = []
    for line_num, line in enumerate(program, start=1):
        for bit in line:
            if bit == "printa":
                ast.append({
                    'program_line': line_num,
                    'operand': ["PRINT", OP_PRINT, 0]
                })
            elif bit[:-1] == "add":
                ast.append({
                    'program_line': line_num,
                    'operand': ["ADD", OP_ADD, int(bit[3:])]
                })
            elif bit[:-1] == "sub":
                ast.append({
                    'program_line': line_num,
                    'operand': ["SUB", OP_SUB, int(bit[3:])]
                })
            elif bit[:-1] == "mult":
                ast.append({
                    'program_line': line_num,
                    'operand': ["MUL", OP_MUL, int(bit[4:])]
                })
            elif bit[:-1] == "div":
                ast.append({
                    'program_line': line_num,
                    'operand': ["DIV", OP_DIV, int(bit[3:])]
                })
            elif bit == "endl":
                ast.append({
                    'program_line': line_num,
                    'operand': ["ENDL", OP_ENDL]
                })
            elif isinstance(int(bit), int):
                ast.append({
                    'program_line': line_num,
                    'operand': ["INT", OP_INT, int(bit)]
                })

    #flags, helps the program know whats happenning
    print_arithmetic_flag = False
    add_flag = [False, 0]
    sub_flag = [False, 0]
    mul_flag = [False, 0]
    div_flag = [False, 0]
    makeshift_stack = []
    for i in range(len(ast)):
        if ast[i]['operand'][1] == OP_PRINT:
            if ast[i]['operand'][2] == 0: # This means we are printing the result of an arithmetic operation
                print_arithmetic_flag = True
        elif ast[i]['operand'][1] == OP_DIV:
            div_flag = [True, ast[i]['operand'][2]]
        elif ast[i]['operand'][1] == OP_MUL:
            mul_flag = [True, ast[i]['operand'][2]]
        elif ast[i]['operand'][1] == OP_ADD:
            add_flag = [True, ast[i]['operand'][2]]
        elif ast[i]['operand'][1] == OP_SUB:
            sub_flag = [True, ast[i]['operand'][2]]
        elif ast[i]['operand'][1] == OP_INT:
            makeshift_stack.append(ast[i]['operand'][2])
        if print_arithmetic_flag == True and len(makeshift_stack) == mul_flag[1] and len(makeshift_stack) >= 2:
            mul_stack = makeshift_stack
            while len(mul_stack) > 1:
                x = mul_stack.pop()
                y = mul_stack.pop()

                mul_stack.append(x*y)
            print(mul_stack[0])
        elif print_arithmetic_flag == True and len(makeshift_stack) == div_flag[1] and len(makeshift_stack) >= 2:
            div_stack = makeshift_stack
            div_stack.reverse()
            while len(div_stack) > 1:
                y = div_stack.pop()
                x = div_stack.pop()

                div_stack.append(y/x)
            print(div_stack[0])
        elif print_arithmetic_flag == True and len(makeshift_stack) == sub_flag[1] and len(makeshift_stack) >= 2:
            subtraction_stack = makeshift_stack
            subtraction_stack.reverse()
            while len(subtraction_stack) > 1:
                y = subtraction_stack.pop()
                x = subtraction_stack.pop()
                
                subtraction_stack.append(y-x)
            print(subtraction_stack[0])
        elif print_arithmetic_flag == True and len(makeshift_stack) == add_flag[1] and len(makeshift_stack) >= 2:
            add_stack = makeshift_stack
            while len(add_stack) > 1:
                y = makeshift_stack.pop()
                x = makeshift_stack.pop()

                add_stack.append(x+y)
            print(add_stack[0])
        elif ast[i]['operand'][1] == OP_ENDL: # DO NOT REMOVE THISTATEMENT
            print_arithmetic_flag = False
            add_flag = [False, 0]
            sub_flag = [False, 0]
            mul_flag = [False, 0]
            div_flag = [False, 0]
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
