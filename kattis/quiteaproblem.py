from sys import stdin
  
for i in stdin:
  
  a = i.splitlines()
  
  for i in a:
    if 'problem' in i.lower():
      print('yes')
    else:
      print('no')
  
    