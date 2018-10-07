import sys

for i in sys.stdin:
  
  a,b = i.split()
  
  a = list(a)
  b = list(b)
  
  newA = []
  newB = []
  
  for i in a:
    newA.insert(0, i)
    
  for i in b:
    newB.insert(0, i)
    
  
  newB = ''.join(newB)
  newA = ''.join(newA)
  
  bothNum = []
  
  bothNum.append(newA)
  bothNum.append(newB)
  bothNum.sort(reverse = True)
  
  print(bothNum[0])