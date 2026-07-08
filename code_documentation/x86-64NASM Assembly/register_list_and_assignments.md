# Registers used in X86-64NASM Assembly
In this file, I'll label each register, and when its used throughout the program so the code can be more readable

## List of all available registers
- RAX - Math operations, system call number, function return value
- RBX - General math, memory addressing
- RCX - Loop counters, shift operations
- RDX - Division (remainder), multiplication (high bits), I/O
- RBP - Stack frame base pointer
- RSP - Stack pointer (top of stack)
- RSI - Source pointer for string operations, memory copying
- RDI - Destination pointer for string operations, memory copying, syscall first argument
- R8 - General purpose, syscall second argument
- R9 - General purpose, syscall third argument
- R10 - General purpose, syscall fourth argument
- R11 - General purpose, syscall fifth argument
- R12 - General purpose
- R13 - General purpose
- R14 - General purpose
- R15 - General purpose
- EAX - Same as RAX but 32-bit
- EBX - Same as RBX but 32-bit
- ECX - Same as RCX but 32-bit
- EDX - Same as RDX but 32-bit
- EBP - Same as RBP but 32-bit
- ESP - Same as RSP but 32-bit
- ESI - Same as RSI but 32-bit
- EDI - Same as RDI but 32-bit
- R8D-R15D - Same as R8-R15 but 32-bit
- AX - Same as RAX but 16-bit
- BX - Same as RBX but 16-bit
- CX - Same as RCX but 16-bit
- DX - Same as RDX but 16-bit
- BP - Same as RBP but 16-bit
- SP - Same as RSP but 16-bit
- SI - Same as RSI but 16-bit
- DI - Same as RDI but 16-bit
- R8W-R15W - Same as R8-R15 but 16-bit
- AL/AH - 8-bit low/high bytes of RAX
- BL/BH - 8-bit low/high bytes of RBX
- CL/CH - 8-bit low/high bytes of RCX
- DL/DH - 8-bit low/high bytes of RDX
- R8B-R15B - 8-bit low bytes of R8-R15

## 64-bit Registers
### R8
The `r8` register is used to store the result of a calculation when encountered in a line of the program. As I'm noticing the isue with this is that there can only be 1 calculation per line, but that could be fixed in the future using parenthesis and stuff.
## 32-bit Registers
### ECX
The `ecx` register is used to store the amount of arguments taken for an arithmetic operation(may be broadened in the future, at the moment its just for that). Doing different operations will use this register as a loop counter.
### EDX
The `edx` register is used to temporialy store the second argument in an arithmetic equation 
