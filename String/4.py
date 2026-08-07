'''
Q4. Count Vowels and Consonants
Difficulty: Easy
Asked In: Wipro, Cognizant, Capgemini
Problem Statement:
Given a string consisting only of English alphabets, count the number of vowels and consonants.
The vowels are:
a, e, i, o, u
All remaining alphabetic characters are considered consonants.
Input:
A single string s.
Output:
Vowels = X
Consonants = Y
Constraints
• The string contains only alphabets.
• 1 <= length <= 10^5

3 ways:
using in operator and by checking every character and using sets
'''

s = input("Enter  a stirng :")

vowel = 0
consonant= 0

for ch in s:
  ch = ch.lower()

  if ch in "aeiouAEIOU":
    vowel +=1
  else:
    consonant +=1

print("vowels =", vowel)
print("consonants =", consonant)

