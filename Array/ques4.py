# # Find the largest element


# Problem: Find the maximum value without using the built-in max() function.
# Input:  [12, 45, 7, 89, 23]
# Output: 89


arr = [12,45,7,89,23]

largest = arr[0]

for num in arr:
  if num > largest :
    largest = num
print(largest)