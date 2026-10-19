# # Question 6. Count even and odd numbers
# # # Problem: Count how many even and odd integers appear in the array.

# Input:  [1, 2, 3, 4, 5, 6]
# Output:
# Even = 3
# Odd = 3

arr = [1,2,3,4,5,6]

even_count = 0
odd_count = 0

for num in arr :
  if num % 2 == 0:
    even_count +=1

  else:
    odd_count += 1

print("Even:", even_count)
print("Odd", odd_count)