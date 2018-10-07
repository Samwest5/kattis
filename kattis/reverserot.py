from sys import stdin

characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')

for i in stdin:
  
  case = i.split()
  
  if int(case[0]) == 0: break
  
  shift = int(case[0])
  
  phrase = case[1]
  
  reverse = phrase[::-1]
  
  encrypted = ''
  
  for char in reverse:
    letterToAdd = characters[(characters.index(char) + shift) % 28]
    encrypted += letterToAdd
    
  print(encrypted)
    

