s = input("enter: ")

i = 0

while i < len(s):
    c = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            c += 1
        j += 1

    if c == 1:
        print(s[i])
        break

    i += 1