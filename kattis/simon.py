import sys

for i in sys.stdin:
 
  if i.strip().isdigit():
    continue
  a = i.split()
    
  if 'says' in a and 'simon' in a:
    a.remove('simon')
    a.remove('says')
    print(' '.join(a).lower())
    
  else:
    print()
