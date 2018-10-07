import sys, math


box = []

for i in sys.stdin:
  if len(i.split()) == 3:
    box.append([float(x) for x in i.split()])
    
  else:
    box.append(float(i))
  

for i in range(1, len(box)):
    if(box[i] > box[0][1] and box[i] > box[0][2] and box[i] > math.sqrt(box[0][1]**2 + box[0][2]**2)):
      print('NE')
    else:
      print('DA')




  
  
  