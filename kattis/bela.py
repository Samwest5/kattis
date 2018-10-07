from sys import stdin

dominantVal = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14
            , '8':0, '7':0}

notDomVal = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0
            , '8':0, '7':0}
            
            
case = []

for i in stdin:
  case.append(i.strip())
  
caseInfo = case[0].split()
dominant = caseInfo[1]

case.pop(0)

total = 0

for hand in case:
  if hand[1] == dominant:
    total += dominantVal[hand[0]]
  else:
    total += notDomVal[hand[0]]

print(total)
