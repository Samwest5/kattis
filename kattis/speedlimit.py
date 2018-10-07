from sys import stdin


cases = []

for i in stdin:
  cases.append([int(x) for x in i.split()])

cases.pop(0)

hours = 0
miles = 0

for case in cases:
  if len(case) is 1:
    print(f'{miles} miles')
    hours = 0
    miles = 0
  else:
    miles += case[0] * (case[1] - hours)
    hours += case[1] - hours
