import sys

teams = []

for i in sys.stdin:
  teams.append(i.split())

teams.pop(0)

schools = []
  
winnerList = []

  
for i in teams:
    
  if len(winnerList) == 12:
    break
    
  if i[0] not in schools:
    schools.append(i[0])
    winnerList.append(i[0] + ' ' + i[1])
      
for i in winnerList:
    print(i)
      