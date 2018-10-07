from sys import stdin

for i in stdin:
  
  if int(i) == 0:
    break
  
  n = i.strip()
  
  p = 10
  
  nSum = sum(int(x) for x in n)
  
  
  pSum = 1 
  
  while(pSum != nSum):
    
    p += 1
    pMult = str(int(n) * p)
    
    pSum = sum(int(x) for x in pMult)
    
  print(p)
    
    