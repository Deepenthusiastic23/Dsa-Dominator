s = input("enter sentence: ")

result = ""
i = 0

while i < len(s):

    if s[i] != " ":
        result = result + s[i]

    i += 1

print(result)