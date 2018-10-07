import sys

stuff = []

for i in sys.stdin:
  
  stuff.append(i.strip())

if len(stuff[0]) >= len(stuff[1]):
  print('go')

else:
  print('no')
  
stuff.clear()