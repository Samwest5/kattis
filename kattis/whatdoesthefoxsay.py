import sys

stuff = []

for i in sys.stdin:
  stuff.append(i.split())

caseList = [[]]
caseListIndex = 0
  
for i in range(len(stuff)):
  
  if stuff[i - 1][0] == 'what':
    caseList.append([])
    caseListIndex += 1
    
  caseList[caseListIndex].append(stuff[i])
  
caseList.pop(0)
caseList[0].pop(0)


for i in caseList:
  others = []
  says = i[0]
  
  for j in i:
    if 'goes' in j:
      others.append(j[2])
  
  if len(others) > 0:    
    for k in others:
      while k in says:
        says.remove(k)
  
  print(' '.join(says))
  others.clear()
  