import sys

vote = {}

for i in sys.stdin:
  
  i = i.strip()
  
  if(i == '***'):
    break
  
  if i not in vote:
    vote[i] = 1
    
  else:
    vote[i] += 1

count = 0

mostVotes = max(vote, key = vote.get)

for name, num in vote.items():
  if(num == vote[mostVotes]):
    count += 1
  if(count == 2):
    break

if(count == 2):
  print("Runoff!")

else:
  print(mostVotes)