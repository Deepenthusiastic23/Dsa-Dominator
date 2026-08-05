'''
Q2. Valid Palindrome
Difficulty: Easy
Asked In: Amazon, Facebook (Meta), Microsoft
Problem Statement:
Given a string s, determine whether it is a palindrome.
A palindrome reads the same forward and backward.
Return True if it is a palindrome; otherwise return False.
Input:
A string s.
Output:
True
or
False
Constraints:
• 1 <= len(s) <= 10^5
# '''


# Example 1 
# Input 
# madam 
# Output 
# True 
 
# Example 2 
# Input 
# python 
# Output 
# False 
 
# Example 3 
# Input 
# racecar 
# Output 
# True 
 
# Follow-up 
# Can you solve it using: 
# • Two pointers?  
# • Without reversing the string? 
#Indexing:


s = input("Enter a string: ")

left = 0
right = len(s)-1

is_palimdrome = True

while left < right:
  if s[left] != s[right]:
    is_palimdrome = False
    break
  left += 1
  right -=1

print(is_palimdrome)