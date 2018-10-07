import sys

for i in sys.stdin:
  
  if(len(i.split()) == 1):
    continue
  
  nums = [int(x) for x in i.split()]
  
  num1 = nums[0]
  num2 = nums[1]
  num3 = nums[2]
  
  if(num1 + num2 == num3):
    print("Possible")
  
  elif(num1 - num2 == num3):
    print("Possible")
    
  elif(num2 - num1 == num3):
    print("Possible")
    
  elif(num1 * num2 ==  num3):
    print("Possible")
    
  elif(num1 / num2 == num3):
    print("Possible")
    
  elif (num2 / num1 == num3):
    print("Possible")
    
  else:
    print("Impossible")