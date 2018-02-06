def median(numbers):
  numbers = sorted(numbers)
  l = len(numbers)
  if l % 2 == 0:
    return (numbers[l//2] + numbers[l//2 - 1]) / 2.0
  else:
    return numbers[l//2]
 
print (median([1, 1, 2]))

from numpy import median

print (median([1, 1, 2]))