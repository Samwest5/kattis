
def swap(myList, a, b):
  myList[a], myList[b] = myList[b], myList[a]

def step1(myList):
  if myList[0] > myList[1]:
    swap(myList, 0, 1)
    print(" ".join(myList))

def step2(myList):
  if myList[1] > myList[2]:
    swap(myList, 1, 2)
    print(" ".join(myList))

def step3(myList):
  if myList[2] > myList[3]:
    swap(myList, 2, 3)
    print(" ".join(myList))

def step4(myList):
  if myList[3] > myList[4]:
    swap(myList, 3, 4)
    print(" ".join(myList))

def step5(myList):
  if " ".join(myList) == "1 2 3 4 5":
    raise SystemExit
    
def sort(myList):
  while True:
    step1(myList)
    step2(myList) 
    step3(myList) 
    step4(myList) 
    step5(myList)


myList = input().split()

sort(myList)

