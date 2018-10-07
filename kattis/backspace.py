skip = 0

str = input()

fixed = ''

for i in range(len(str) - 1, -1, - 1):

  if str[i] == '<':
    skip += 1
  
  elif skip != 0:
    skip -= 1
    continue
  
  else:
    fixed += str[i]
    
fixed = fixed[::-1]
print(fixed)