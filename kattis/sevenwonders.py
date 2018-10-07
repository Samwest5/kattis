import sys

tCount = 0
cCount = 0
gCount = 0

for i in sys.stdin:
    
    score = list(i.strip())
    for i in score:
      if i == 'T':
        tCount += 1
      if i == 'C':
        cCount += 1
      if i == 'G':
        gCount += 1
    
    minCount = min(tCount, cCount, gCount)
    
    print(tCount**2 + cCount**2 + gCount**2 + minCount * 7)
    
    tCount = 0
    gCount = 0
    cCount = 0
    