from random import randint
low = 1
high = 1000

guesses = 10

ans = 'nope'

while guesses > 0:
  mid = int((low + high) / 2)
  print(mid, flush=True)
  response = input()
  if response == 'correct':
    break
  elif response == 'lower':
    high = mid - 1
  elif response == 'higher':
    low = mid + 1
  guesses -= 1