
  
while(True):
  
  list1 = []
  list2 = []
  
  numItems = int(input())
  if numItems == 0: break
  
  for i in range(numItems):
    list1.append(int(input()))
    
  for i in range(numItems):
    list2.append(int(input()))
    
  sorted1 = sorted(list1)
  
  sorted2 = sorted(list2)
  
  corresponding = {}
  
  for i in range(len(sorted1)):
    corresponding[sorted1[i]] = sorted2[i]
    
  proper2 = []
  
  for i in list1:
    proper2.append(corresponding[i])
    
  for i in proper2:
    print(i)
    
  print()
    