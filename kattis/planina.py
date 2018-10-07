import sys

for i in sys.stdin:
  
  a = int(i)
  
  b = 2**a + 1
  
  print(b**2)
  