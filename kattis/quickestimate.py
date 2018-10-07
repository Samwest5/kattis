import sys

estimates = []

for i in sys.stdin:
  estimates.append(i.strip())

for i in range(1, len(estimates)):
  print(len(estimates[i]))
  
  