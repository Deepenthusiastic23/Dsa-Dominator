n = int(input("Enter numnber of rows :"))

for i in range(1, n+1):
  print(" " * (n-i) + str(i) * (2 * i - 1))