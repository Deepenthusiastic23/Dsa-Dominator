'''Asked In: Infosys, Accenture
Problem Statement
Given a string containing lowercase English letters, convert every lowercase letter to
uppercase without using Python's built-in upper() method.'''

s = input("Enter your text: ")

result = ""

for ch in s:
    result += chr(ord(ch) - 32)

print(result)