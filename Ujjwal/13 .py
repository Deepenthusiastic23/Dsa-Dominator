'''Asked In: TCS Digital, Infosys, Accenture
Problem Statement
Given a sentence, count the number of words.
Ignore:
• Leading spaces
• Trailing spaces
• Multiple spaces between words '''

s = input("Enter your text:")

words = s.split()

print(len(words))