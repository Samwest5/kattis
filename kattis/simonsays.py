import sys

for i in sys.stdin:
 
  if i.strip().isdigit():
    continue
  a = i.split()
    
  if 'says' in a and 'Simon' in a:
    a.remove('Simon')
    a.remove('says')
    print(' '.join(a).lower())
    
    