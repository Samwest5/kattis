import sys

stuff = []

for i in sys.stdin:
  
  a = [int(x) for x in i.split()]
  
  stuff.append(a)

p1 = sum(stuff[0])

p2 = sum(stuff[1])

if p1 > p2:
  print('Gunnar')
  
elif p1 == p2:
  print("Tie")

else:
  print('Emma')