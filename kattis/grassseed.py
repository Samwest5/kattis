import sys

lawnStuff = []

for i in sys.stdin:
  
  a = [float(x) for x in i.split()]
  
  lawnStuff.append(a)
  
cost = lawnStuff[0][0]

lawnStuff.pop(0)
lawnStuff.pop(0)

area = 0;

for i in lawnStuff:
  
  area += i[0] * i[1]
  

totalCost = area * cost

print(totalCost)


  
  