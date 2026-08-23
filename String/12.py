# Reverse Words in a String 

def reverse_words(s):
  result = []
  word = ""

  i = len(s) -1


  while i >= 0:
    # extra spaces skip 

    while i >= 0 and s[i] == " ":
      i -= 1

    #  collecting words

    word =""

    while i >= 0 and s[i] != " ":
        word = s[i] + word
        i -= 1

        #  If word get 

    if word:
       result.append(word)

  return " " .join(result)


s = input("Enter a string: ")
print(reverse_words(s))