import calendar
import datetime

def weekday_count(s,e):
  s_date = datetime.datetime.strptime(s,'%d/%m/%Y')##assigning strat and end date 
  e_date = datetime.datetime.strptime(e,'%d/%m/%Y')##using datetime using datetime library 
  week = {}
  for i in range((e_date-s_date).days):
    day = calendar.day_name[(s_date + datetime.timedelta(days=i+1)).weekday()]
    week[day] = week[day] + 1 if day in week else 1
  return week ##counting number of weeks, every week will add one number of day
## if week is not complete then number of days will be returned
print(weekday_count("01/01/1990", "31/12/2000"))