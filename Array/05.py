# find the smallest 
# Input:  [12, 45, 7, 89, 23]
# Output: 7


arr = [12,45,7,89,23]

smallest = arr[0]

for num in arr:
  if num < smallest:
    smallest = num

print(smallest)
