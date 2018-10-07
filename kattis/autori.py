import sys

for i in sys.stdin:
  names = i.split('-')
  
  pretty = []
  
  for i in names:
    pretty.append(i[0])
    
  print(''.join(pretty))