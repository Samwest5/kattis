import sys

stuff = []

for i in sys.stdin:
  
  if i.strip().isdigit():
    stuff.append(int(i))
  else:
    stuff.append(' ')
    
stuff.pop(0)
stuff.pop(0)

caseIndex = 0
caseList = [[]]

for i in stuff:
  if i == ' ':
    caseIndex += 1
    caseList.append([])
    continue
  caseList[caseIndex].append(i)
  
candySum = 0
totalKids = 0

for case in caseList:
  candySum = 0
  for i in range(len(case)):
    if i == 0:
      totalKids = case[i]
      continue
    candySum += case[i]
  if candySum % totalKids == 0:
    print('YES')
  else:
    print('NO')
    candySum = 0


 
