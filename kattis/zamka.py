import sys

limits = []

for i in sys.stdin:
  if(i == '\n'):
    break
  limits.append(int(i))

possible = []

for i in range(limits[0], limits[1] + 1):
  if limits[2] == sum(int(x) for x in str(i)):
    possible.append(i)

print(min(possible))
print(max(possible))
