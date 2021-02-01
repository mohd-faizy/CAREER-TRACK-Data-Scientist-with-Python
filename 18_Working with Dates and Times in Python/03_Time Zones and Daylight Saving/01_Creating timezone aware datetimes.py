'''
01 - Creating timezone aware datetimes

----------------------------------------------------
- Import timezone.
- Set the tzinfo to UTC, without using timedelta.
----------------------------------------------------
'''
# Import datetime, timezone
from datetime import datetime, timedelta, timezone

# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)

# Print results
print(dt.isoformat())

# Output: 2017-10-01T15:26:26+00:00

'''
----------------------------------------------------
- Set pst to be a timezone set for UTC-8.
- Set dt's timezone to be pst.
----------------------------------------------------
'''

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

# Output: 2017-10-01T15:26:26-08:00

'''
----------------------------------------------------
- Set tz to be a timezone set for UTC+11.
- Set dt's timezone to be tz.
----------------------------------------------------
'''
# Create a timezone for Australian Eastern Daylight Time, or UTC+11
aedt = timezone(timedelta(hours=11))

# October 1, 2017 at 15:26:26, UTC+11
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=aedt)

# Print results
print(dt.isoformat())

# Output: 2017-10-01T15:26:26+11:00
