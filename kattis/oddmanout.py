import sys

caseNum = 1

for i in sys.stdin:
  
  letsParty = i.split()
  
  if len(letsParty) > 1:
    for j in letsParty:
      if letsParty.count(j) == 1:
        print(f'Case #{caseNum}: {j}')
        caseNum += 1
