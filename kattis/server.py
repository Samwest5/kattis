import sys

stuff = []

for i in sys.stdin:
  
  stuff.append([int(x) for x in i.split()])

time = stuff[0][1]

tasks = stuff[1]

currTime = 0 
taskNum = 0

for i in tasks:
  if currTime + i > time:
    break
  else:
    currTime += i 
    taskNum += 1
    
print(taskNum)