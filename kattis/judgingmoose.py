import sys

for i in sys.stdin:
  
  moose = [int(x) for x in i.split()]
  
  moose.sort(reverse=True)
  
  if moose[0] == 0 and moose[1] == 0:
    print("Not a moose")
    
  elif moose[0] != moose[1]:
    print(f'Odd {moose[0] * 2}')
    
  else:
    print(f'Even {moose[0] * 2}')
  