import sys

unordered = []

ordered = []

setNum = 0

for i in sys.stdin:
  
  if(i.strip() == '0'):
    break
  
  if(i.strip().isdigit()):
    unordered.append([])
    unordered[setNum].append(f'SET {setNum + 1}')
    setNum += 1
    
  else:
    unordered[setNum - 1].append(i.strip())
    
for i in range(len(unordered)):
  
  ordered.append([])
  ordered[i].append(unordered[i][0])
  
  for j in range(1, len(unordered[i]), 2):
    ordered[i].append(unordered[i][j])
    
    
  if len(unordered[i]) % 2 != 0:
    for j in range(len(unordered[i]) -1, 0, -2):
      ordered[i].append(unordered[i][j])
      
  else:
    for j in range(len(unordered[i]) - 2, 1, -2):
      ordered[i].append(unordered[i][j])


for i in range(len(ordered)):
  for j in range(len(ordered[i])):
    print(ordered[i][j])