import sys

rawL = []

tripsTracker = []

trip = -1

for i in sys.stdin:
  
    rawL.append(i.strip())

rawL.pop(0)

for i in rawL:
    if(i.isdigit()):
        trip += 1 
        tripsTracker.append([])
        continue
    
    tripsTracker[trip].append(i)
  
for i in tripsTracker:
    print(len(set(i)))