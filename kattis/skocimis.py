import sys
for i in sys.stdin:
  a,b,c = i.split()
  a = int(a)
  b = int(b)
  c = int(c)
  print(max(b - a, c - b) - 1)