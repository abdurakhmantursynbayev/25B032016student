from datetime import datetime, timedelta, timezone
import calendar
from math import ceil

a = input()
a = a.replace("UTC", "").replace(":","")

b = input()
b = b.replace("UTC", "").replace(":","")

a_date = datetime.strptime(a, "%Y-%m-%d %z")
b_date = datetime.strptime(b, "%Y-%m-%d %z")
y = b_date.year; m = a_date.month; d = a_date.day
if m == 2 and d == 29 and not calendar.isleap(y):
    d = 28
candidate = a_date.replace(year = y, month = m, day = d)
if candidate.astimezone(timezone.utc) < b_date.astimezone(timezone.utc):
    y +=1
    if m == 2 and d == 29 and not calendar.isleap(y):
        d = 28
    candidate = a_date.replace(year = y, month = m, day = d)
difference = candidate.astimezone(timezone.utc) - b_date.astimezone(timezone.utc)
total = (difference.total_seconds()) / 86400
total = ceil(total)
print(total)