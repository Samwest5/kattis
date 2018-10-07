inp = input()
hour, minute = inp.split()
hour = int(hour)
minute = int(minute)


  
if minute < 45 and hour == 0:
  print(f'23 {60 - (45 - minute)}')
  
elif minute >= 45:
  print(f'{hour} {minute - 45}')
  
elif minute < 45:
  print(f'{hour - 1} {60 - (45 - minute)}')
  



