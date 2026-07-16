'''Asked In: Amazon, Adobe, Walmart
Problem Statement
Given a string s, remove all duplicate characters while preserving the order of their first occurrence.
Return the resulting string.'''

s = input("Enter your text:")

visited = set()
result = ""

for ch in s:
    if ch not in visited:
        result += ch
        visited.add(ch)

print(result)