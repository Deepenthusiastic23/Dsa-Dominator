# '''
# Q3. Find the Length of a String Without Using len()
# Difficulty: Easy
# Asked In: Infosys, Accenture, Wipro
# Problem Statement:
# Given a string s, determine its length without using Python's built-in len() function.
# Input 
# A string s. 
 
# Output 
# Return the total number of characters. 
 
# Constraints 
# • 1 <= length <= 10^5  
 
# Example 1 
# Input 
# Python 
# Output 
# 6 
 
# Example 2 
# Input 
# Interview 
# Output 
# 9 
 
# Follow-up 
# Can you solve it in O(n) time? 
 

s = input("Enter a string: ")

count = 0

for ch in s:
  count += 1

print(count)