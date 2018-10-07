import sys

numbers = []

for i in sys.stdin:
  
  modNum = int(i) % 42
  
  if modNum not in numbers:
    numbers.append(modNum)
    
print(len(numbers))