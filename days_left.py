
from datetime import date, timedelta

#initializing the start Date
Date = date(2026, 10, 19)
print( "Start Date: ", Date)

#getting the End Date
EndDate = Date  + timedelta(weeks=34)


TotalDays = (EndDate - Date).days
DaysLeft = (EndDate - date.today()).days
percentage_Completed = (TotalDays - DaysLeft) / TotalDays * 100

print("Days Left: ", DaysLeft, "Percentage completed: ", round(percentage_Completed, 2),"%")
