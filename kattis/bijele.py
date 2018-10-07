import sys


changes = []

for i in sys.stdin:
  
  numList = [int(x) for x in i.split()]
  
  changes.append(1 - numList[0])
  changes.append(1 - numList[1])
  changes.append(2 - numList[2])
  changes.append(2 - numList[3])
  changes.append(2 - numList[4])
  changes.append(8 - numList[5])
  for i in changes:
    print(i, end=' ')
  
  
  