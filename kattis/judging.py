length = int(input())

judge = {}

kattis = {}

for i in range(length):
  result = input()
  if result not in judge:
    judge[result] = 1
  else:
    judge[result] += 1
  
for i in range(length):
  result = input()
  if result not in kattis:
    kattis[result] = 1
  else:
    kattis[result] += 1
  
foShow = 0
for i in judge:
  if i in kattis:
    foShow += min(judge[i], kattis[i])
print(foShow)