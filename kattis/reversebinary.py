import sys

for i in sys.stdin:
  
  a = format(int(i), 'b')
 
  b = ''
 
  for i in a:
    b = i + b
    
  c = int(b, 2)
  
  print(c)
   
  