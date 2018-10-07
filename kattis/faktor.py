import sys

stuff = []

for i in sys.stdin:
  
  stuff.append([int(x) for x in i.split()])

a = 0 

numArticle = float(stuff[0][0])
impact = float(stuff[0][1])

while a / numArticle  < impact - .999:
  a += 1
  
print(a)