# Given a string s, reverse the string and return the reversed string.
# You are not allowed to use any built-in reverse function.

s = input("Enter your Text: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

print(reverse)