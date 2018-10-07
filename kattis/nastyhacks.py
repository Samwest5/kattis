import sys

nums = []

for i in sys.stdin:
  nums.append(str(i).strip())
  
for i in range(1, len(nums)):
  
  line = nums[i].split()
  
  r = int(line[0])
  
  e = int(line[1])
  
  c = int(line[2])
  
  if(r == e - c):
    print("does not matter")
    
  elif(r > e - c):
    print("do not advertise")
    
  elif( r < e - c):
    print("advertise")
    