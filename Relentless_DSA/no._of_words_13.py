s = input("enter: ")

count = 1
i = 0

while i < len(s):
    if s[i] == " ":
        count += 1
    i += 1

print("Words =", count)