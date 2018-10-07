import sys

stuff = []

for i in sys.stdin:
  stuff.append([int(x) for x in i.split()])

batt = []

for i in stuff[1]:
  if i != -1:
    batt.append(i)
    
print(sum(batt) / len(batt))
  