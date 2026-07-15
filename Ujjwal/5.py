'''Asked In: Amazon, Deloitte, TCS Digital
Problem Statement
Given a string s, count how many times each character appears in the string.
Return the frequency of every character.'''

s = input("Enter The Text: ")

freq = {}

for ch in s:

    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1

for key in freq:
    print(key, ":", freq[key])