from sys import stdin
names  = []
orders = []
orderList = {}
stuff = []

for i in stdin:
  stuff.append(i.split())


del stuff[0]

for line in stuff:
  if line[0].isdigit():
    orders.sort()
    names.sort()
    for food in orders:
      print(food, end=" ")
      for name in names:
        if food in orderList[name]:
          print(name, end=" ")
      print()
    orders.clear()
    names.clear()
    orderList.clear()
    print()
  else:
    orderList[line[0]] = line[1:]
    for food in line[1:]:
      if food not in orders:
        orders.append(food)
    if line[0] not in names:
      names.append(line[0])