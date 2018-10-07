import sys

for i in sys.stdin:
  check = False
  
  word = i
  
  for i in range(len(word) - 1):
    if word[i] == 's' and word[i] == word[i + 1]:
      print('hiss')
      check = True
      break
  
  if check == False:
    print('no hiss')
  
  
  
  
  
  