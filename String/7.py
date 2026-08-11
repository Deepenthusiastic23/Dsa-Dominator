# Input 
#    Hello World 
# Output 
# HelloWorld 
 
# Example 3 
# Input 
# Open   AI 
# Output 
# OpenAI 
 
# Follow-up 
# Can you solve it without using replace()? 
 
# Question 7: Check if Two Strings are Equal 
# Difficulty:   Easy 
# Asked In: Infosys, Capgemini, Tech Mahindra 
# Problem Statement 
# Given two strings s1 and s2, determine whether they are exactly equal. 
# Return: 
# • "Equal" if both strings are identical.  
# • "Not Equal" otherwise.  
# Comparison is case-sensitive. 
 
# Input 
# Two strings. 
 
# Output 
# Equal 
# or 
# Not Equal 
 
# Constraints 
# • 1 <= len(s1), len(s2) <= 10^5  
 
# Example 1 
# Input 
# abc 
# abc 
# Output 
# Equal 
 
# Example 2 
# Input 
# Python 
# python 
# Output 
# Not Equal 
 
# Example 3 
# Input 
# hello 
# hello1 
# Output 
# Not Equal 
 
# Follow-up 
# Can you compare the strings without using the == operator?



s1 = input()
s2 = input()

if len(s1) != len(s2):
  print("Not Equal")
else:
  equal = True


  for i in range (len(s1)):
    if s1[i] != s1[i]:
      equal = False
      break

  if equal:
    print("Equal")
  else:
    print("Not Equal")