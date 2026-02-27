from datetime import datetime, timezone, timedelta

a = input()
a_hms = a[11:19]
a = a[0:11] + a[19:]
a_hms = datetime.strptime(a_hms, "%H:%M:%S")
a = a.replace("UTC", "").replace(":","")
b = input()
b_hms = b[11:19]
b = b[0:11] + b[19:]

b_hms = datetime.strptime(b_hms, "%H:%M:%S")
b = b.replace("UTC", "").replace(";","")
a_date = datetime.strptime(a, "%Y-%m-%d %z")
b_date = datetime.strptime(b, "%Y-%m-%d %z")
a_date = a_date.replace(hour = a_hms.hour, minute = a_hms.minute, second = a_hms.second)
b_date = b_date.replace(hour = b_hms.hour, minute = b_hms.minute, second = b_hms.second)
total = b_date.astimezone(timezone.utc) - a_date.astimezone(timezone.utc)
totals = int(total.total_seconds())
print(totals)