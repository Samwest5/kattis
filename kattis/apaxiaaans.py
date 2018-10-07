import sys
word = input()

new = ""
prev = ""

for character in word:
  if character != prev:
    new += prev
    prev = character 
new += prev 
print(new)
  
    
  