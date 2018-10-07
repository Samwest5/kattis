import sys

inpt = []

for i in sys.stdin:
  
  inpt.append(i.split())
  
count = 0  
  
for i in inpt[1]:
    if(int(i) < 0):
        count += 1
    
print(count)
  
  

  

  
  