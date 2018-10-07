import sys

stuff = []

for i in sys.stdin:
  
  stuff.append(i.strip())
  
stuff.pop(0)

for i in range(0, len(stuff), 2):
  differences = []
  for j in range(len(stuff[i])):
    if(stuff[i][j] != stuff[i + 1][j]):
      differences.append('*')
    else:
      differences.append('.')
  print(stuff[i])
  print(stuff[i + 1])
  print(''.join(differences))
  print()