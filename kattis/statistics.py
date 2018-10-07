import sys

caseNum = 0

for i in sys.stdin:
  
  caseNum += 1
  
  nums = [int(n) for n in i.split()]
  
  minX = nums[1]
  maxX = nums[1]
  
  for i in range(len(nums)):
    
    if(i == 0):
      continue
    
    if(nums[i] > maxX):
      maxX = nums[i] 
    
    if(nums[i] < minX):
      minX = nums[i]
      
  rangeX = maxX - minX
  
  print(f"Case {caseNum}: {minX} {maxX} {rangeX}")