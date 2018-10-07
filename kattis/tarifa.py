from sys import stdin

stuff = []

for i in stdin:
  stuff.append(int(i))
  

monthly = stuff[0]
saved = monthly
stuff.pop(0)
stuff.pop(0)
for i in stuff:
  saved += monthly - i
  
print(saved)
  