# Registers used in X86-64NASM Assembly
In this file, I'll label each register, and when its used throughout the program so the code can be more readable
## Functions
### .add_loop
This function takes care of addition within the program
### .print_arithmetic_loop
This function handles the print arithmetic function which prints any number
## Man-Made Variable
### bufferNum
This variable resveres 21 bytes, and is used when printing numbers with the print arithmetic keyword
## 64-bit Registers
### R8
The `r8` register is used to store the result of a calculation when encountered in a line of the program. As I'm noticing the isue with this is that there can only be 1 calculation per line, but that could be fixed in the future using parenthesis and stuff.
## 32-bit Registers
### ECX
The `ecx` register is used to store the amount of arguments taken for an arithmetic operation(may be broadened in the future, at the moment its just for that). Doing different operations will use this register as a loop counter.
### EDX
The `edx` register is used to temporialy store the second argument in an arithmetic equation 
