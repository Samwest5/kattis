from sys import stdin

for i in stdin:
  word = i.strip()
  wordSplit = [word[i:i+3] for i in range(0, len(word), 3)]
  changes = 0
  
  for sub in wordSplit:
    if sub[0] != 'P':
      changes += 1
    if sub[1] != 'E':
      changes += 1
    if sub[2] != 'R':
      changes += 1
      
  print(changes)
  