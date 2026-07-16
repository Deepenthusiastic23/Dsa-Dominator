'''Asked In: Amazon, Microsoft, Oracle
Problem Statement
Given a string containing words separated by spaces, reverse the order of the words.
• Remove extra spaces.
• Keep only one space between words. '''

s = input("Enter your text:")

words = s.split()

result = ""

for i in range(len(words)-1, -1, -1):
    result += words[i]

    if i != 0:
        result += " "

print(result)