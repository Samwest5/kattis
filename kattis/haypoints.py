from sys import stdin

values = {}

stuff = []

entries, cases = [int(x) for x in input().split()]

for i in range(entries):
  keyWord, worth = input().split()
  worth = int(worth)
  values[keyWord] = worth

  currCase = ''
  line = ''
  
while(cases > 0):
  
  line = input()
  
  if line == '.':
    for i in currCase.split():
      if i in values:
        total += values[i]
    print(total)
    currCase = ''
    cases -= 1;
    continue
  
  
  currCase += ' ' + line
  total = 0
  
  