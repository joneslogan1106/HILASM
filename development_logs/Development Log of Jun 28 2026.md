# Goals for Todat
- [ ] Start working on assembly equivlant
- [ ] A working "console" to dest different commands w/ error handling.

So I consulted a local expert on assembly/copilot, and I asked how I would implement a stack, and I got this result.
```asm
; x86-64 assembly (NASM syntax) example
; Assemble with: nasm -f elf64 stack_example.asm
; Link with: ld stack_example.o -o stack_example

section .data
    msg db "Stack Example", 0

section .bss
    ; reserve space for 1024 bytes stack size manually (optional)
    my_stack resb 1024

section .text
    global _start

_start:
    ; Initialize RSP to top of our custom stack (optional)
    lea rsp, [my_stack + 1024]

    ; Push values onto the stack
    mov rax, 10
    push rax          ; push 10 onto the stack
    mov rax, 20
    push rax          ; push 20 onto the stack

    ; Pop value from the stack
    pop rbx           ; rbx = 20
    pop rcx           ; rcx = 10

    ; Example: perform addition using the stack
    mov rax, 5
    push rax
    mov rax, 7
    push rax

    pop rdx            ; rdx = 7
    pop rax            ; rax = 5
    add rax, rdx       ; rax = 12

    ; Exit program (Linux syscall)
    mov rax, 60       ; syscall: exit
    xor rdi, rdi      ; exit code 0
    syscall
```

After looking at this code, I realized I was ovrcomplicating things, a lot. All I need to use is the `mov` keyword and I'm good, so I'm going to implement that.
O and btw It seems that I need to make even more versions of this program to account for more compilers, yay.
