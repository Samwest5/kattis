import sys 

for i in sys.stdin:
  
  people, chicken = i.split()
  
  people = int(people)
  chicken = int(chicken)
  
  if(people - chicken == 1):
    print("Dr. Chaz needs 1 more piece of chicken!")
    continue
  
  if(chicken < people):
    print(f"Dr. Chaz needs {people - chicken} more pieces of chicken!")
  
  if(chicken - people == 1):
    print("Dr. Chaz will have 1 piece of chicken left over!")
    continue
  
  if(chicken > people):
    print(f"Dr. Chaz will have {chicken - people} pieces of chicken left over!")