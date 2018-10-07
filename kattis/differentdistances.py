import math, sys

for i in sys.stdin:
  
  
  nums = [float(x) for x in i.split()]
  
  if len(nums) == 1:
    break
  x1 = nums[0]
  y1 = nums[1]
  x2 = nums[2]
  y2 = nums[3]
  p = nums[4]
  
  print((abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p))