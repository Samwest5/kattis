import sys
from math import pi

for i in sys.stdin:
  
  totalR, crustR = i.split()
  totalR = int(totalR)
  crustR = int(crustR)
  
  totalArea = pi * totalR**2
  cheeseArea = pi * (totalR - crustR)**2

  
  print((cheeseArea / totalArea) * 100)
  
  


  