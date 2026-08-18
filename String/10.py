# first non repeating character 

def first_non_repeating(s):
  freq = {}

  # count frequency 
  for ch in s:
    freq[ch] = freq.get(ch, 0)+1


  # find first character qpperaing once

  for ch in s:
    if freq[ch] == 1:
      return ch

  return -1






print(first_non_repeating("leetcode"))
print(first_non_repeating("loveleetcode"))
print(first_non_repeating("aabbcc"))

