# 1 
# 3 2 
# 6 5 4
# 10 9 8 7
# 14 13 12 11
n = int(input("Enter number of row: "))

num = 1

for i in range(1, n+1):
  num = num + i - 1

  for j in range(i):
    print(num-j, end = " ")
  print()

  num = num +1