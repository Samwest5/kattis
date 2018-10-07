import sys

stuff = []

for i in sys.stdin:
  
  stuff.append(i.strip())
  
stuff.pop(0)

won = 0

for battle in stuff:
  for move in range(len(battle) - 1):
    if battle[move] == 'C'and battle[move + 1] == 'D':
      won -= 1
      break
  won += 1
print(won)