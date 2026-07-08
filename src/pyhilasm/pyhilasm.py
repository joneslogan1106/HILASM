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
def generate_ast(program):
    ast = []
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

    return ast

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

    ast = generate_ast(program) # Creates an "AST" which is semi-human readable
    print_arithmetic_flag = False
    add_flag = [False, 0]
    sub_flag = [False, 0]
    mul_flag = [False, 0]
    div_flag = [False, 0]
    makeshift_stack = []
    for i in range(len(ast)):
        operand = ast[i]['operand'][1]
        if operand == OP_PRINT:
            if ast[i]['operand'][2] == 0: # This means we are printing the result of an arithmetic operation
                print_arithmetic_flag = True
        elif operand == OP_DIV:
            div_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_MUL:
            mul_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_ADD:
            add_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_SUB:
            sub_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_INT:
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


def compile_x86_64_nasm():
    program = [
        ["printa", "add2", "4", "5", "endl"],
        ["printa", "sub2", "10", "9", "endl"],
        ["printa", "mult2", "10", "5", "endl"],
        ["printa", "div2", "500", "10", "endl"], 
        ["printa", "sub3", "5", "9", "3", "endl"],
        ["printa", "add3", "2", "5", "8", "endl"],
        ["printa", "mult3", "59", "9", "38", "endl"], 
        ["printa", "div3", "500", "10", "2", "endl"]
    ]
    ast = generate_ast(program)

    print_arithmetic_flag = False
    add_flag              = [False, 0]
    sub_flag              = [False, 0]
    mul_flag              = [False, 0]
    div_flag              = [False, 0]
    makeshift_stack       = []
    
    code = """section .bss
\tbufferNum resb 21 ; Gives 21 bytes of buffer space for max 64-bit int
section .text
\tglobal _start

print_arithmetic_loop:
\txor rdx, rdx ; frees up the rdx register before division
\tdiv rbx ; divides rdx:rax by 10 where rax is the quotient, and rdx is the raimnder
\tadd dl, '0' ; converts remainder digit to ASCII
\tdec rcx ; move buffer point backward
\tmov [rcx], dl ; store ascii character in buffer
\ttest rax, rax ; check if quotient is 0
\tjnz print_arithmetic_loop ; if not 0 loop again to get next digit

\t; string lenth calc
\t; length formula: (base addr +20) - current pointer
\tmov rdx, bufferNum ; load base addr into rdx
\tadd rdx, 20 ; add 20
\tsub rdx, rcx ; subtract current pointer positon

\t; sys_write syscall
\tmov rax, 1 ; sys_write
\tmov rdi, 1 ; stdout
\tmov rsi, rcx ; rsi = actual first digit
\tsyscall

.add_loop:
\tpop rdx ; moves the value from the top of the stack into edx

\tadd r8, rdx
\tdec ecx ; amount of numbers being added
\tjnz .add_loop


_start:
\tmov r8, 0 ; calculation result
\tmov ecx, 0 ; this is the amount of numbers being added in a arithmetic operation
    """
    for i in range(len(ast)):
        operand = ast[i]['operand'][1]
        if operand == OP_PRINT:
            if ast[i]['operand'][2] == 0:
                print_arithmetic_flag = True
        elif operand == OP_DIV:
            div_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_MUL:
            mul_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_ADD:
            add_flag = [True, ast[i]['operand'][2]]
            code += f"\t; sets the argument number for addition to {ast[i]['operand'][2]}\n\tmov ecx, {ast[i]['operand'][2]} ; sets the amount of numbers expected in an addition equation\n"
        elif operand == OP_SUB:
            sub_flag = [True, ast[i]['operand'][2]]
        elif operand == OP_INT:
            code += f"\t; push {ast[i]['operand'][2]}\n\tpush {ast[i]['operand'][2]}\n"
            makeshift_stack.append(ast[i]['operand'][2])
        elif operand == OP_ENDL:
            print_arithmetic_flag = False
            add_flag              = [False, 0]
            sub_flag              = [False, 0]
            mul_flag              = [False, 0]
            div_flag              = [False, 0]
            makeshift_stack       = []
        if len(makeshift_stack) == add_flag[1] and len(makeshift_stack) >= 2:
            # python code below
            # add_stack = makeshift_stack
            # while len(add_stack) > 1:
            #   y = makeshift_stack.pop()
            #   x = makeshift_stack.pop()
            #   add_stack.append(x+y)

            code += """\t; print adding
\tmov rax, r8 ; number being printed
\tmov rcx, bufferNum ; point rcx to end of buffer
\tadd rcx, 20 ; point it to the full end of the buffer
\tmov byte [rcx], 10 ; divisor always set to 10
\tjmp print_arithmetic_loop ; calls the print loop
"""

        if print_arithmetic_flag == True and len(makeshift_stack) == add_flag[1] and len(makeshift_stack) >= 2:
            pass

    code += "\tmov rax, 60 ; syscall: exit\n\txor rdi, rdi ; exit code 0\n\tsyscall"

    print(code)
# Basic command line styuff
def command_line_utils():
    if sys.argv[1] == "help":
        print("""usage: ./pyhilasm.py program_file [args]
sim - Simulates a program file
cx86NASM - Compiles program according to the x86 ISA(NASM Syntax)""")
        exit(0)
    elif sys.argv[1] == "sim":
        simulate_program()
    elif sys.argv[1] == "cx86-64NASM":
        compile_x86_64_nasm()
    else:
        print("Not found")
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No arguments provided. Try running `help`")
        exit(1)
    else:
        command_line_utils()
