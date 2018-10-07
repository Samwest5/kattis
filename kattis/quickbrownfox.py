import sys

stuff = []

alphabet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])



for i in sys.stdin:
 
  stuff.append(i.strip())
  
found = set([])

stuff.pop(0)

for phrase in stuff:
  for letter in phrase:
    if letter.lower() in alphabet:
      found.add(letter.lower())
  if len(alphabet - found) == 0:
    print('pangram')
    found.clear()
    
  else:
    missing = sorted(list(alphabet - found))
    print(f"missing {''.join(missing)}")
    found.clear()
    
