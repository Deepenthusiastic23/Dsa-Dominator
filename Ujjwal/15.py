'''Asked In: Google, Apple, Adobe
Problem Statement
Given a string consisting of repeated characters, compress it by replacing each sequence of the same
character with the character followed by its count.
If the compressed string is not shorter than the original string, return the original string.'''

s = input("Enter your text:")

result = ""
count = 1

for i in range(1, len(s)):

    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

result += s[-1] + str(count)

if len(result) < len(s):
    print(result)
else:
    print(s)