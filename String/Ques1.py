# 1. Problem Statement 
# Given a string s, reverse the string and return the reversed string. 
# You are not allowed to use any built-in reverse function. 
 
# Input 
# A single string s. 
# Output 
# Return the reversed string. 
 
# Constraints 
# • 1 <= len(s) <= 10^5  
# • The string contains English letters, digits, and special characters.  
 
# Example 1 
# Input 
# hello 
# Output 
# olleh 
 
# Example 2 
# Input 
# Python 
# Output 
# nohtyP 
 
# Example 3 
# Input 
# 12345 
# Output 
# 54321 
 
# Follow-up 
# Can you solve it using: 
# • Two pointers?  
# • Without using extra space?  
# #  

s = list(input())


left = 0
right = len(s) -1

while left < right:
  s[left],s[right] = s[right], s[left]

  left += 1
  right -= 1
print("" .join(s))