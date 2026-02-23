from datetime import datetime, timedelta

now = datetime.now()

# Add time
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
two_hours_later = now + timedelta(hours=2, minutes=30)

print(f"Now:             {now}")
print(f"Tomorrow:        {tomorrow}")
print(f"Next week:       {next_week}")
print(f"2.5 hours later: {two_hours_later}")

# Subtract time
yesterday = now - timedelta(days=1)
print(f"Yesterday:       {yesterday}")