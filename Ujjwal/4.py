'''Asked In: Wipro, Cognizant, Capgemini
Problem Statement
Given a string consisting only of English alphabets, count the number of vowels and consonants.
The vowels are:
a, e, i, o, u
All remaining alphabetic characters are considered consonants'''


s = input("Enter your text: ").lower()

vowels = 0
consonants = 0

for ch in s:

    if ch in "aeiou":
        vowels += 1

    else:
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)