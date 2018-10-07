from sys import stdin

vowels = 'aeiouy'

for i in stdin:
  
  phrase = i.split()
  newWords = []
  
  for word in phrase:
    if word[0] in vowels:
      newWords.append(word + 'yay')
      continue
    else:
      vowelIndex = 0
      switchToBack = ''
      for i in range(len(word)):

        if word[i] in vowels:
          break
        switchToBack += word[i]
        vowelIndex += 1
      newWords.append(word[vowelIndex:] + switchToBack + 'ay')
  
  print(' '.join(newWords))
      
        
        