'''Asked In: Amazon, Meta, Microsoft
Problem Statement
Given a string s, find the first character that appears exactly once.
If no such character exists, return -1.'''

s = input("Enter your Text:")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
else:
    print(-1)