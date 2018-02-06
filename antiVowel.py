vowel = ['a','e','i','o','u']

def anti_vowel(text):
  res = ""
  for c in text:
    if c.lower() not in vowel:
      res += c
  return res

print (anti_vowel("Hey You!"))