vowel = 'aeiou'

encrypted = input().split()

decrypted = ''

for word in encrypted:
  ignore = 0
  decryptedWord = ''

  for letter in word:
  
    if ignore > 0:
      ignore -= 1
      continue
  
    if letter in vowel:
      ignore = 2
    
    decryptedWord += letter
    
  decrypted += ' ' + decryptedWord
  
print(decrypted[1:])