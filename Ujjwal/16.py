'''Asked In: Adobe, Amazon, Oracle
Problem Statement
Given two strings s and goal, return True if and only if s can become goal after performing any
number of left rotations on s.
A left rotation moves the first character of the string to the end.
For example:
"abcde"
After one left rotation:
"bcdea"
After two left rotations:
"cdeab"'''

s = input("Enter your text:")
goal = input("Enter your goal of text:")

if len(s) != len(goal):
    print(False)

elif goal in (s + s):
    print(True)

else:
    print(False)