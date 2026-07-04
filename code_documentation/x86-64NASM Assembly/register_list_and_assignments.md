# Registers used in X86-64NASM Assembly
In this file, I'll label each register, and when its used throughout the program so the code can be more readable
## 32-bit Registers
### EAX
The `eax` register is used to store the result of a calculation when encountered in a line of the program. As I'm noticing the isue with this is that there can only be 1 calculation per line, but that could be fixed in the future using parenthesis and stuff.
### ECX
The `ecx` register is used to store the amount of arguments taken for an arithmetic operation(may be broadened in the future, at the moment its just for that). Doing different operations will use this register as a loop counter.
