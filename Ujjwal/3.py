'''Asked In: Infosys, Accenture, Wipro
Problem Statement
Given a string s, determine its length without using Python's built-in len() function.'''

s = input("Enter your Text: ")
count = 0
for char in s:
    count += 1
print(count)