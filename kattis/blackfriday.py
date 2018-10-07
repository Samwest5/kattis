dumb = [1, 1, 1, 5, 3, 4, 6, 6]

sz = input()

rolls = [int(x) for x in input().split()]

rollsTuples = []

for i in range(len(rolls)):
  rollsTuples.append((rolls[i], i))
  
sortedTuples = sorted(rollsTuples, reverse = True)

for i in sortedTuples:
  check = 0
  for j in sortedTuples:
    if i[0] == j[0]:
      check += 1
  if check == 1:
    print(i[1] + 1)
    exit()

print('none')