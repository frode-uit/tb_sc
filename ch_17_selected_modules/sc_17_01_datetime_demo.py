# file: sc_17_01_datetime_demo.py


from datetime import datetime, timezone
# Creating datetime objects from the current time
now_local = datetime.now()                  # local time
now_utc = datetime.now(timezone.utc)        # UTC time

print("Now (local):", now_local) # Now (local): 2026-01-23 11:45:12.123456
print("Now (UTC):  ", now_utc)   # Now (UTC):   2026-01-23 10:45:12.123789+00:00

# Creating datetime objects from specific date and time
dt1 = datetime(2023, 3, 15, 12, 30, 0)  # naive datetime
dt2 = datetime(2023, 3, 15, 12, 30, 0, tzinfo=timezone.utc)  # aware datetime
print("Specific datetime (naive):", dt1)  # Specific datetime (naive): 2023-03-15 12:30:00
print("Specific datetime (UTC):  ", dt2)  # Specific datetime (UTC):  2023-03-15 12:30:00+00:00

# Creating datetime from timestamp
timestamp = 1678881000.0  # corresponds to 2023-03-15 12:30:00 UTC
dt_from_timestamp = datetime.fromtimestamp(timestamp, tz=timezone.utc)
print("Datetime from timestamp (UTC):", dt_from_timestamp)  # Datetime from timestamp (UTC): 2023-03-15 12:30:00+00:00
print("Current timestamp:", datetime.now().timestamp())  # Current timestamp: <current time in seconds>

# Parsing datetime from string
dt_str = "2023-03-15 12:30:00"
dt3 = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", dt3)  # Parsed datetime: 2023-03-15 12:30:00
# Formatting datetime to string
formatted_str = dt3.strftime("%d/%m/%Y %I:%M %p")
print("Formatted datetime string:", formatted_str)  # Formatted datetime string: 15/03/2023 12:30 PM

# Obtaining the same as time.time()
timestamp = dt3.timestamp()
print("Timestamp:", timestamp)  # Timestamp: 1678881000.0

# datetime arithmetic
dt4 = dt3.replace(year=2024)
print("Replaced year:", dt4)  # Replaced year: 2024-03-15 12:30:00

# datetime and timedelta arithmetic
from datetime import timedelta
dt5 = dt3 + timedelta(days=10, hours=5)
print("Datetime after adding 10 days and 5 hours:", dt5)  # Datetime after adding 10 days and 5 hours: 2023-03-25 17:30:00

