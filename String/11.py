def remove_duplicates(s):
  seen = set()
  result = ""

  for ch in s :
    if ch not in seen:
      seen.add(ch)

      result += ch

  return result

s  = input()
print(remove_duplicates(s))