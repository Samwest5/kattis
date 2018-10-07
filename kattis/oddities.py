import sys

nums = []

for i in sys.stdin:
  nums.append(int(i))
  
for i in range(1,len(nums)):
  if(nums[i] % 2 == 0):
    print(f'{nums[i]} is even')
    
  else:
    print(f'{nums[i]} is odd')
