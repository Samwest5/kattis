import sys 

for i in sys.stdin:
  
  numer,denom = i.split()
  numer = int(numer)
  denom = int(denom)
  if denom == 0: break;

  print(f"{numer // denom} {numer % denom} / {denom}")