# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

n= int(input("Enter no of rows :"))

for i in range(1, n+1):
  for j in range (1, i+1):
    if (i+ j) % 2 ==0:
      print(1, end= " ")
    else:
      print (2, end=" ")
  print()