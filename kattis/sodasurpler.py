start, found, cost = [int(x) for x in input().split()]

cans = start + found

sodas = 0

while(cans >= cost):
  
  bought = cans // cost
  
  sodas += bought
  
  cans = bought + (cans % cost)
  
print(sodas)