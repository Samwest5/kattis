from sys import stdin

for i in stdin:
  
  if len(i.split()) == 1:
    continue
  
  grades = [int(x) for x in i.split()]
  
  sumGrades = 0
  numStudents = grades.pop(0)
  
  for j in grades:
    sumGrades += j 
    
  avg = float(sumGrades) / numStudents
  
  aboveAvgCount = 0
  
  for grade in grades:
    if grade > avg:
      aboveAvgCount += 1
  
  aboveAvg = 100 * aboveAvgCount / numStudents
  
  print("%.3f" % aboveAvg + "%")
  
  
  