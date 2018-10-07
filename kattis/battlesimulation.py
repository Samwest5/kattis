
counter = {'R': 'S', 'B': 'K', 'L': 'H'}

# rbl c 

attackMoves = list(input().upper())


defencesMoves = ''

i = 0

while i < len(attackMoves):
  
  if i + 2 < len(attackMoves) :
  
    if(
        attackMoves[i] == 'R' and
        attackMoves[i + 1] == 'L' and
        attackMoves[i + 2] == 'B'
      ):
      
      defencesMoves += 'C'
      i = i + 3
      continue
    
    if(
        attackMoves[i] == 'R' and
        attackMoves[i + 1] == 'B' and
        attackMoves[i + 2] == 'L'
      ):
      
      defencesMoves += 'C'
      i = i + 3
      continue
    
    if(
        attackMoves[i] == 'B' and
        attackMoves[i + 1] == 'L' and
        attackMoves[i + 2] == 'R'
      ):
      
      defencesMoves += 'C'
      i = i + 3
      continue
    
    if(
        attackMoves[i] == 'B' and
        attackMoves[i + 1] == 'R' and
        attackMoves[i + 2] == 'L'
      ):
      
      defencesMoves += 'C'
      i = i + 3
      continue
    
    if(
        attackMoves[i] == 'L' and
        attackMoves[i + 1] == 'B' and
        attackMoves[i + 2] == 'R'
      ):
      
      defencesMoves += 'C'
      i = i + 3
      continue
    
    if(
        attackMoves[i] == 'L' and
        attackMoves[i + 1] == 'R' and
        attackMoves[i + 2] == 'B'
      ):
      
      defencesMoves += 'C'
      i = i + 3
      continue
    
 
  defencesMoves += counter[attackMoves[i]]
  i += 1
    
print(defencesMoves)