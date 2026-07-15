s1 = input("enter 1st string: ")
s2 = input("enter 2nd string: ")

if len(s1) != len(s2):
    print("not Equal")

else:
    i = 0

    while i < len(s1):

        if s1[i] != s2[i]:
            print("Not equal")
            break

        i += 1

    else:
        print("Equal")