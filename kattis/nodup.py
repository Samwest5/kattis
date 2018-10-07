import sys

check = True

for i in sys.stdin:
  
  words = i.split()
  
  for i in words:
    if words.count(i) > 1:
      print('no')
      check = False
      break
  
  if check == True:
    print('yes')