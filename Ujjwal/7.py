'''Asked In: Infosys, Capgemini, Tech Mahindra
Problem Statement
Given two strings s1 and s2, determine whether they are exactly equal.
Return:
• "Equal" if both strings are identical.
• "Not Equal" otherwise.
Comparison is case-sensitive.'''

s1 = input("Enter Your text s1: ")
s2 = input("Enter your text s1: ")

if len(s1) != len(s2):
    print("not equal")

else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print("not equal")
            break
    else:
        print("Equal")