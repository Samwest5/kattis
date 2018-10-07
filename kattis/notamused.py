from sys import stdin

day = 0

visitors = {}

for i in stdin:
  
  event = i.split()
  
  if event[0] == 'OPEN':
    day += 1
    
  if event[0] == 'CLOSE':
    print(f'Day {day}')
    for key in sorted(visitors.keys()):
      print(f"{key} ${format(visitors[key] * .10, '.2f')}")
    print()
    visitors.clear()
  
  if event[0] == 'ENTER':
    if event[1] not in visitors:
      visitors[event[1]] = - int(event[2])
    else:
      visitors[event[1]] -= int(event[2])
    
  if event[0] == 'EXIT':
    visitors[event[1]] += int(event[2])
    
      
