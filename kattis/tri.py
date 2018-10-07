import sys

for i in sys.stdin:
  
  a,b,c = i.split()
  a = int(a)
  b = int(b)
  c = int(c)
  
  
  
  if a == (b + c):
      print(f"{a}={b}+{c}")
      
  elif a == (b - c):
      print(f"{a}={b}-{c}")
      
  elif a == (b * c):
      print(f"{a}={b}*{c}")
      
  elif (c != 0) and (a == (b / c)):
    print(f"{a}={b}/{c}")
      
  elif (a + b) == c:
      print(f"{a}+{b}={c}")
      
  elif (a - b) == c:
      print(f"{a}-{b}={c}")
      
  elif (a * b) == c:
      print(f"{a}*{b}={c}")
      
  else:
    print(f"{a}/{b}={c}")
 
