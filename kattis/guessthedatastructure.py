from sys import stdin

class Stack:
  def __init__(self):
    self.data = []

  def pop(self):
    return self.data.pop(0)

  def push(self, number):
    self.data.insert(0, number)

  def isEmpty(self):
    if not self.data:
      return True

  def reset(self):
    self.data.clear()
  

class Queue:
  def __init__(self):
    self.data = []

  def pop(self):
    return self.data.pop(-1)

  def push(self, number):
    self.data.insert(0, number)

  def isEmpty(self):
    if not self.data:
      return True

  def reset(self):
    self.data.clear()


class PriorityQueue:
  def __init__(self):
    self.data = []

  def pop(self):
    return self.data.pop(-1)

  def push(self, number):
    self.data.append(number)
    self.data.sort()

  def isEmpty(self):
    if not self.data:
      return True

  def reset(self):
    self.data.clear()


isStack = True
isQueue = True
isPriorityQueue = True
testCount = 3

stackTest = Stack()
queueTest = Queue()
pqueueTest = PriorityQueue()

firstline = True

for line in stdin:
  line = [int(x) for x in line.split()]
  if len(line) == 1:
    if firstline:
      firstline = False
      continue

    if testCount > 1:
      print("not sure")

    elif testCount == 0:
      print("impossible")

    elif isStack:
      print("stack")

    elif isQueue:
      print("queue")

    else:
      print("priority queue")

    stackTest.reset()
    queueTest.reset()
    pqueueTest.reset()
    isStack = True
    isQueue = True
    isPriorityQueue = True
    testCount = 3
    continue

  commandType = line[0]
  x = line[1]

  if commandType == 1:

    stackTest.push(x)
    queueTest.push(x)
    pqueueTest.push(x)
  
  else:

    if stackTest.isEmpty() or stackTest.pop() != x:
      if isStack:
        testCount -= 1
        isStack = False
  
    if queueTest.isEmpty() or queueTest.pop() != x:
      if isQueue:
        testCount -= 1
        isQueue = False

    if pqueueTest.isEmpty() or pqueueTest.pop() != x:
      if isPriorityQueue:
        testCount -= 1
        isPriorityQueue = False

if testCount > 1:
  print("not sure")

elif testCount == 0: 
  print("impossible")

elif isStack:
  print("stack")

elif isQueue:
  print("queue")

else:
  print("priority queue") 

