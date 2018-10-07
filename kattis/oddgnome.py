import sys


stuff = []

for i in sys.stdin:
  
  a = [int(x) for x in i.split()]  
  stuff.append(a)

stuff.pop(0)

for i in stuff:
  if len(i) == 3:
    print(2)
  
  else:
    for j in range(1, len(i)):
      if i[j] + 1 != i[j + 1]:
        print(j + 1)
        break
    