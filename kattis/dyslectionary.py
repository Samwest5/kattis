from sys import stdin
from operator import itemgetter


def printWithPadding(words):
  maxPadding = max(len(w) for w in words)
  for word in words:
    padding = " " * (maxPadding - len(word))
    print(f"{padding}{word[::-1]}")

wordList = []

for i in stdin:
  word = i.strip()
  word = word[::-1]
  wordList.append(word)

wordList.append('*')

currList = []

for item in wordList:
  if item == '' or item == '*':
    currList.sort()
    printWithPadding(currList)
    currList.clear()
    if item == '*':
      break
    print()
    continue
  currList.append(item)