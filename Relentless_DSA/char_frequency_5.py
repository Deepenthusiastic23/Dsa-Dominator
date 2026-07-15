s = input("enter a string: ")

i = 0

while i < len(s):

    count = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            count += 1
        j += 1

    print(s[i], "=", count)

    i += 1