import sys

stuff = []

for i in sys.stdin:
  
  stuff.append(i.strip())
  

security = int(stuff[0])

original = stuff[1]

check = stuff[2]


if security % 2 == 0:
  passed = True
  for i in range(len(original)):
    if original[i] != check[i]:
      passed = False
  if passed:
    print('Deletion succeeded')
  else:
    print('Deletion failed')
  
else:
  passed = True
  for i in range(len(original)):
    if original[i] == check[i]:
      passed = False
  if passed:
    print('Deletion succeeded')
  else:
    print('Deletion failed')
  