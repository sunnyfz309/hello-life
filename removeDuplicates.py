def remove_duplicates(l):
  res = []
  for i in l:
    if i not in res:
      res.append(i)
  return res

print (remove_duplicates([1, 1, 2, 2]))

def remove_duplicates2(l):
  return list(set(l))

print (remove_duplicates2([1, 1, 2, 2]))