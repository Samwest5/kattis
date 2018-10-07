import sys

stuff = []

for i in sys.stdin:
  
  stuff.append(i.split())

stuff[0] = [int(x) for x in stuff[0]]
stuff[0].sort()

myDict = {'A': stuff[0][0], 'B': stuff[0][1], 'C': stuff[0][2]}

order = list(stuff[1][0])

for i in order:
  print(myDict[i], end=' ')