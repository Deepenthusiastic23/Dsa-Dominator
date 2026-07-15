'''Asked In: Amazon, Google, Microsoft
Problem Statement
Given two strings s and t, determine whether t is an anagram of s.
Two strings are anagrams if they contain the same characters with the same frequencies,
but the order of characters may differ.
Return True if they are anagrams; otherwise return False.
'''

s = input("Enter your text:")
t = input("Enter your text:")

if len(s) != len(t):
    print(False)

else:
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            print(False)
            break

        freq[ch] -= 1

        if freq[ch] < 0:
            print(False)
            break

    else:
        print(True)