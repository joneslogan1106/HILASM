# Goals for Today
- [x] Fix previous bug with division
- [x] A working simulated program
- [ ] Start working on assembly equivlant
- [ ] A working "console" to test different commands w/ error handling

Today I'm going to try to implement an x86 assembly version of this program. (Most likely using godbolt and C)
Link to Godbolt env used for today: https://godbolt.org/z/71YocWvhG
Actual code inputted into godbolt:
```c
#include <stdio.h>

int main() {
    int stack[] = [4,5];
    printf("%d", stack[0]);

    return 0;
}
```

(x86-64 gcc 16.1)
```asm
.LC0:
        .string "%d"
"main":
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     DWORD PTR [rbp-8], 4
        mov     DWORD PTR [rbp-4], 5
        mov     eax, DWORD PTR [rbp-8]
        mov     esi, eax
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    "printf"
        mov     eax, 0
        leave
        ret
```

Lookng at this its obvious that I need to include `LC0` due to`printa` being a keyword.

Going to take a break for now and come back later
