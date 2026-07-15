'''Asked In: Amazon, Facebook (Meta), Microsoft
Problem Statement
Given a string s, determine whether it is a palindrome.
A palindrome reads the same forward and backward.
Return True if it is a palindrome; otherwise return False.
'''

s = input("Enter your text: ")
if s[::-1] == s:
    print("True")

else:
    print("False")