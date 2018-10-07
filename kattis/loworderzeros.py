from sys import stdin

dig= [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def lastNonZeroDigit(n):
  if n < 10:
    return dig[n]

  if ((n//10)%10)%2 == 0:
    return (6*lastNonZeroDigit(n//5)*dig[n%10]) % 10
  else:
    return (4*lastNonZeroDigit(n//5)*dig[n%10]) % 10
  return 0

for case in stdin:
  if case.strip() == '0':
    continue
  print(lastNonZeroDigit(int(case)))

