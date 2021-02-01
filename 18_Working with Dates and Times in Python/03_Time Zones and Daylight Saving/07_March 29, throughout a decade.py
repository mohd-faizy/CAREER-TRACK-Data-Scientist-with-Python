'''
07 - March 29, throughout a decade

Daylight Saving rules are complicated: they're different in different 
places, they change over time, and they usually start on a Sunday (and 
so they move around the calendar).

For example, in the United Kingdom, as of the time this lesson was written, 
Daylight Saving begins on the last Sunday in March. Let's look at the UTC 
offset for March 29, at midnight, for the years 2000 to 2010.

Instructions

- Using tz, set the timezone for dt to be 'Europe/London'.
- Within the for loop:
- Use the .replace() method to change the year for dt to be y.
- Call .isoformat() on the result to observe the results.
'''
# Import datetime and tz
from datetime import datetime
from dateutil import tz

# Create starting date
dt = datetime(2000, 3, 29, tzinfo=tz.gettz('Europe/London'))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year=y).isoformat())

'''
As you can see, the rules for Daylight Saving are not trivial. When in doubt, 
always use tz instead of hand-rolling timezones, so it will catch the Daylight 
Saving rules (and rule changes!) for you.

<script.py> output:
    2000-03-29T00:00:00+01:00
    2001-03-29T00:00:00+01:00
    2002-03-29T00:00:00+00:00
    2003-03-29T00:00:00+00:00
    2004-03-29T00:00:00+01:00
    2005-03-29T00:00:00+01:00
    2006-03-29T00:00:00+01:00
    2007-03-29T00:00:00+01:00
    2008-03-29T00:00:00+00:00
    2009-03-29T00:00:00+00:00
    2010-03-29T00:00:00+01:00
'''
