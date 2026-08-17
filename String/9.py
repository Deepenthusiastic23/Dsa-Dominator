# Valid Anagram

s = input().strip()
t = input().strip()


if len(s) !=  len(t):
  print(False)

else:
  freq = [0] * 26

  for ch in s : 
    freq[ord(ch) -ord('a')] += 1

  for ch in t:
    freq[ord(ch) -ord('a')]  -=1


  print(all(count == 0 for count in freq))