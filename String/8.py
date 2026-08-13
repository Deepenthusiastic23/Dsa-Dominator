# Question 8: Convert Lowercase to Uppercase Without Using upper() 
# Difficulty:   Easy 
# Asked In: Infosys, Accenture 
# Problem Statement 
# Given a string containing lowercase English letters, convert every lowercase letter to 
# uppercase without using Python's built-in upper() method. 
 
# Input 
# A lowercase string. 
 
# Output 
# Return the uppercase version. 
 
# Constraints 
# • 1 <= len(s) <= 10^5  
 
# Example 1 
# Input 
# python 
# Output 
# PYTHON 
 
# Example 2 
# Input 
# deepak 
# Output 
# DEEPAK 
 
# Example 3 
# Input 
# amazon 
# Output 
# AMAZON 
 
# Follow-up 
# Can you convert characters using their ASCII values? 
 

s = input("Enter a string:")

result  =" "

for ch in s:
  if "a" <= ch <= "z":
    result += chr(ord(ch) -32)

  else:
    result += ch
print(result)
