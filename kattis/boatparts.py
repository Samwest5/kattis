parts,days = [int(x) for x in input().split()]

partsReplaced = set([])

for i in range(days):
  part = input()
  if part not in partsReplaced:
    partsReplaced.add(part)
  if len(partsReplaced) == parts:
    print(i + 1)
    exit()
print("paradox avoided")
