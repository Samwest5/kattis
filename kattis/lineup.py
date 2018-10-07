import sys

stuff = []

for i in sys.stdin:
  
  stuff.append(i.strip())

stuff.pop(0)

incr = sorted(stuff)

decr = sorted(stuff, reverse = True)

if stuff[0] == incr[0] and stuff[len(stuff) -1] == incr[len(incr) -1]:
  print('INCREASING')
  
elif stuff[0] == decr[0] and stuff[len(stuff) -1] == decr[len(incr) -1]:
  print('DECREASING')
  
else:
  print('NEITHER')
  