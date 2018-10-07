import sys

whiteSpace = ['_']

lowerCase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in sys.stdin:
  
  whiteSpaceCount = 0
  lowerCaseCount = 0
  upperCaseCount = 0
  symbolCount = 0
  
  totalCharacters = len(i) - 1
  
  for character in i.strip():
    if character in whiteSpace:
      whiteSpaceCount += 1
    elif character in lowerCase:
      lowerCaseCount += 1
    elif character in upperCase:
      upperCaseCount += 1
    else:
      symbolCount += 1
      
  whiteSpacePercentage = whiteSpaceCount / totalCharacters
  lowerCasePercentage = lowerCaseCount / totalCharacters
  upperCasePercentage = upperCaseCount / totalCharacters
  symbolPercentage = symbolCount / totalCharacters
    
  print(whiteSpacePercentage)
  print(lowerCasePercentage)
  print(upperCasePercentage)
  print(symbolPercentage)