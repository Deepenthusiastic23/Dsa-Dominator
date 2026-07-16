'''Asked In: Capgemini, Wipro, Oracle
Problem Statement
Given a sentence, find the longest word.
If multiple words have the same maximum length, return the first one.'''

s = input("Enter your text:")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)