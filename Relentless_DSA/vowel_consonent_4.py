s = input("enter sentence: ")

i = 0
vowel = 0
consonant = 0

while i < len(s):

    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        vowel += 1
    else:
        consonant += 1

    i += 1

print("Vowels =", vowel)
print("Consonants =", consonant)