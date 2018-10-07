import sys

num = []

for i in sys.stdin:
  if(i == ''):
    break
  num.append(str(i.strip()))
  
sumNum = 0
  
for i in range(1, len(num)):
  sumNum += int(num[i][:-1])**int(num[i][-1])

print(sumNum)
