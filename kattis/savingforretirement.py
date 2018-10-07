import sys

for i in sys.stdin:
  
  b, bR, bS, a, aS = i.split()
  
  b = int(b)
  bR = int(bR)
  bS = int(bS)
  a = int(a)
  aS = int(aS)

  bMoney = (bR - b) * bS
  
  aR = a + (bMoney // aS) + 1
  
  print(aR)
  
    