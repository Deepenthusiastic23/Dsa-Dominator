s = input("enter sentence: ")

w = ""
i = len(s)-1

while i >= 0:
    if s[i] != " ":
        w = s[i] + w
    else:
        print(w, end=" ")
        w = ""
    i -= 1

print(w)