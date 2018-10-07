import sys, datetime 

weekdayDict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
              
for i in sys.stdin:
  
  day, month = [int(x) for x in i.split()]
  print(weekdayDict[datetime.date(2009, month, day).weekday()])
  


  