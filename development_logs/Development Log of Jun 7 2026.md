# Development Log of Jun 7
Goals for today:
- [ ] A working simulated program
- [ ] Start assembly equivalent
- [ ] Start C Development
- [ ] A working "console" to test different commands
- [x] Fix yesterday's bug.

Going off of yesterday's development, it seems that I had an error on clearing the stack, so I need to fix that. The fix was turning an `elif` statement into an `if` statement. UPDATE: I have no clue what I did it just fixed itself.

## Implementation of Subtraction Operation
I'm just going to copy and paste what I did for addition, I need to keep in mind that order is backwards, because of stack. I'm now realizing I've only made it able to handle two numbers. *Oh freak*. Ok so I have a working test of two numbers, now I need to handle any numbers.

What I'm thinking is:
```psuedocode
arguments = operation[index with arguments]
makeshift stack = [9,3,4,4,4,4]
while stack != 0:

```

I'm actually stuck on this so Ima take a break.
