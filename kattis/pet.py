import sys

score = [0,1]

scorePos = 1

for i in sys.stdin:
  
  a = [int(x) for x in i.split()]
  
  count = sum(a)
  
  if count > score[0]:
    score[0] = count
    score[1] = scorePos
    
  scorePos += 1
  
print(score[1], end=' ')
print(score[0])
  