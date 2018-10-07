moves = list(input())

location = ['a','b','c']

for i in moves:
  
  if i == 'A':
    temp = location[0]
    location[0] = location[1]
    location[1] = temp
    
  if i == 'B':
    temp = location[1]
    location[1] = location[2]
    location[2] = temp
    
  if i == 'C':
    temp = location[0]
    location[0] = location[2]
    location[2] = temp
    
for i in range(len(location)):
  if location[i] == 'a':
    print(i + 1)
    