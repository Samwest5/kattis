import sys

translate = {}

for i in sys.stdin:


  if(len(i.split()) == 1):
    pig = i.split()
    if pig[0] not in translate:
      print('eh')
    else:
      print(translate[pig[0]])
    
  if(len(i.split()) == 2):
    english, pig = i.split()
    translate.update({pig: english})