import sys

maths = []

for i in sys.stdin:
  
  maths.append(i.strip())

maths.pop(0)


for i in maths:
  if i == 'P=NP':
    print('skipped')
    
  else:
    argument = i.split('+')
    print(int(argument[0]) + int(argument[1]))
    