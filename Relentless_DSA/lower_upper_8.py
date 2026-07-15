s = input("enter: ")

a = ""
i = 0

while i < len(s):
    if 'a' <= s[i] <= 'z':
        a += chr(ord(s[i]) - 32)
    else:
        a += s[i]
    i += 1

print(a)