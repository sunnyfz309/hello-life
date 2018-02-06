def reverse(text):
  str = ""
  for c in text:
    str = c + str
  return str

s = "Python!"
print (reverse(s))
print (s[::-1])
print (''.join(reversed(s)))