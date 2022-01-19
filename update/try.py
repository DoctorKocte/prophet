import datetime
from datetime import timedelta
from datetime import date, timedelta

format = "%Y-%m-%d %H:%M:%S"
start_date = date(2021, 10, 27) 
start = datetime.datetime(2021, 10, 27, 0, 0, 0)
end = datetime.datetime(2021, 10, 29, 0, 0, 0)
delta = (end - start)
minutes = 0

for k in range(delta.days + 1):
    day = (start_date + timedelta(days=k)).strftime(format)
    for i in range(48):
        print(((start) + timedelta(minutes=minutes)).strftime(format))
        minutes += 30




