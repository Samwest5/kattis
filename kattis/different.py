import sys

for i in sys.stdin:
  a = [int(x) for x in i.split()]
  
  print(abs(a[0] - a[1]))