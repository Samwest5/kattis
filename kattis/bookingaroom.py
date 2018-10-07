import sys

takenRooms = []

for i in sys.stdin:
    
    if(len(i.split()) == 1):
      takenRooms.append(int(i))
    
    if(len(i.split()) == 2):
      totalRooms, takenNum = (int(j) for j in i.split())
      
roomsList = []

for i in range(1, totalRooms + 1):
  roomsList.append(i)
  
if(len(roomsList) == takenNum):
     print('too late')

else:
    for i in takenRooms:
        roomsList.remove(i)
    print(roomsList[0])
