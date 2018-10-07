import sys

alphabet = {'a': '@', 'b': '8', 'c': '(', 'd': '|)','e': '3','f': '#', 'g': '6', 'h': '[-]', 'i': '|', 'j': '_|', 'k': '|<', 'l': '1', 'm': '[]\/[]', 'n': '[]\[]', 'o': '0', 'p': '|D', 'q': '(,)', 'r': '|Z', 's': '$', 't': "']['", 'u': '|_|', 'v': '\/', 'w': '\/\/', 'x': '}{', 'y': '`/', 'z': '2'}

for i in sys.stdin:
  
  sentence = i
  convertedL = []
  
  for i in sentence:
    if i.lower() in alphabet:
      convertedL.append(alphabet[i.lower()])
    else:
      convertedL.append(i)
      
  print(''.join(convertedL))
  
  