import sys

stuff = []

for i in sys.stdin:
  
  stuff.append([int(x) for x in i.split()])
  
stuff.pop(0)

for i in stuff:
  if i[0] % 400 != 0:
    print((i[0] // 400) + 1)
  
  else:
    print(i[0] // 400)
    