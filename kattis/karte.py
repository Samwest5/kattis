
string = input()

deck = [string[i:i+3] for i in range(0, len(string), 3)]

seen = set([])

fullDeck = {'P': 13, 'K': 13, 'H': 13, 'T': 13}

for i in deck:
  if i in seen:
    print('GRESKA')
    exit()
  
  fullDeck[i[0]] -= 1 
  
  seen.add(i)
  
if fullDeck['P'] > 0:
  print(fullDeck['P'], end = ' ')
  
if fullDeck['K'] > 0:
  print(fullDeck['K'], end = ' ')
  
if fullDeck['H'] > 0:
  print(fullDeck['H'], end = ' ')
  
if fullDeck['T'] > 0:
  print(fullDeck['T'], end = ' ')
  
  


  
  

    



  
  