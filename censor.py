def censor(text, word):
  strs = text.split(" ")
  for i in range(len(strs)):
    if strs[i] == word:
      strs[i] = "*" * len(word)
  return " ".join(strs)

print (censor("this hack is wack hack", "hack"))