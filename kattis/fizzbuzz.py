import sys

for i in sys.stdin:
  
  nums = [int(x) for x in i.split()]
  
  for i in range(1, nums[2] + 1):
    if i % nums[0] == 0 and i % nums[1] == 0:
      print('FizzBuzz')
      
    elif i % nums[0] == 0:
      print('Fizz')
      
    elif i % nums[1] == 0:
      print('Buzz')
      
    else:
      print(i)
    