from datetime import datetime, timedelta
from math import floor

a = input()
a = a.replace("UTC", "").replace(":", "")
b = input()
b = b.replace("UTC", "").replace(":", "")
a_date = datetime.strptime(a, "%Y-%m-%d %z")
b_date = datetime.strptime(b, "%Y-%m-%d %z")
total_seconds = abs(a_date - b_date)
s = (total_seconds.total_seconds()) / 86400
s = floor(s)
print(s)