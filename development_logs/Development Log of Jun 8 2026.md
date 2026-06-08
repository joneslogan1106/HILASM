# Development Log Jun 8
Goals for today:
- [ ] A working simulated program
- [ ] Start assembly equivlant
- [ ] Start C Development
- [ ] A working "console" to test different command

Yesterday I took a break after trying to find a solution to adding x amount of number of integers. I'm thinking ofthis way:
```psuedocode
add_flag = True
makeshift_stack = [9,3,3,3]

if sub found:
    reversed_stack = makeshift_stack.reverse()
    while len(makeshift_stack) != 1:
        y = reversed_stack.pop()
        x = reversed_stack.pop()

        reversed_stack.append(y-x)

[5,9,3] -> [3,9,5] -> y = 5, x = 9. y-x=-4 -> [3, -4] -> y = -4, x=-3, y-x=-7
[5,9,3,4] -> [4,3,9,5] -> y = 5, x = 9, y-x=-4 -> [4,3,-4] -> y = -4, x=3, y-x=-7 -> [4,-7] -> y = -7, x = 4, y-x=-11 -> [11]
```
