# Daily Development Log - Jun 4 2026
For today I'm choosing a type of syntax that I like, which will be difficult, but heres what I'm currently trying to settle for in a program:
```hilasm
printa add2 4 5 endl
```
Where printa stands for "print arithmetic" such as addition, subtraction, multiplication, etc.m Then add2 adds two different numbers, and is derived from the command "add" which takes an argument(number right next to it) such as "add3", "add4" etc.

In the code, currently line 43 in "pyhilasm.py" note there is logic that states:
```python
numbered_program.append([program.index(line) + 1, [OP_PRINT, 0]])```
This logic is currently saying which line the program line is currently on, then adds its identifier(the print iota) then 0, meaning we are printing the result of an arithmetic operation. This pattern continues for each command that is like this(which should be explained in the actual code)
