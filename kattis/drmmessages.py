from sys import stdin

def rotationValue(string):
  total = sum([ord(i)-65 for i in string])
  return total
  
def rotateLetter(letter, rotations):
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  newLetterIndex = (ord(letter) - 65 + rotations) % 26
  return alphabet[newLetterIndex]
  
# def rotateLetter(letter, rotations):
#   rotationsLeft = rotations
#   currPos = ord(letter) - 65
#   while rotationsLeft != 0:
#     currPos += 1
#     if currPos == 26:
#       currPos = 0
#     rotationsLeft -= 1
#   return chr(currPos + 65)
  
  
def merge(string1, string2):
  mergedString = ''
  for i in range(0, len(string1)):
    mergedString += rotateLetter(string1[i], ord(string2[i]) - 65)
  return mergedString


for i in stdin:
  encrypted = i.strip()
  firstHalf = encrypted[:int(len(encrypted)/2)]
  secondHalf = encrypted[int(len(encrypted)/2):]
  
  newFirst = ''
  newSecond = ''
  
  firstHalfRotation = rotationValue(firstHalf)
  secondHalfRotation = rotationValue(secondHalf)
  
  # for i in firstHalf:
  #   newFirst += rotateLetter(i, firstHalfRotation)
    
  # # for i in secondHalf:
  # #   newSecond += rotateLetter(i, secondHalfRotation)
    
  newFirst = ''.join([rotateLetter(i, firstHalfRotation) for i in firstHalf])
  
  newSecond = ''.join([rotateLetter(i, secondHalfRotation) for i in secondHalf])
  
  
  decrypted = merge(newFirst, newSecond)
  print(decrypted)
  



  
  







