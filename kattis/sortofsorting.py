a = []
first = True
while True:
  numCases = int(input())
  if numCases == 0:
    break
  a.clear()
  for i in range(numCases):
    a.append(input())
  a.sort(key=lambda x:(x[0]+x[1]))
  if first:
    first = False
  else:
    print()
  
  for blah in a:
    print(blah)
