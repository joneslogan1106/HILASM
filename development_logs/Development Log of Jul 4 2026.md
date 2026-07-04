# Goals for Today
- [ ] Fix yesterday's bug
- [ ] Implement other operations in assembly
- [ ] Implement a consol to test different comands
- [ ] Document code so it makes sense

In order to actually understand the bug I need to do research on a stack in x86-NASM Assembly
## Research on stacks in NASM X86-64 ASM
You can push 32 bit numbers directly to the stack, if the number is larger then 32 bits you must move that value into a register then push that reggister onto the stack.
I can actually restructure the current push logic to handle these numbers I believe. 
Also note that the default stack pointer is the rsp register, and those registers automaticially

Also note I made a file in order to identify each register. Also I removed all things I did not uflly understand yet
