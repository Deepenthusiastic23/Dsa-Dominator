s = input("enter string:  ")

a = ""
i = 0

while i < len(s):

    if s[i] not in a:
        a = a + s[i]

    i += 1

print(a)