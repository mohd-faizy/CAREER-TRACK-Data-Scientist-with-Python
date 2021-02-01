'''
03 - What time did the bike leave in UTC?

Having set the timezone for the first ten rides that W20529 took, let's 
see what time the bike left in UTC. We've already loaded the results of 
the previous exercise into memory.

Instructions

- Within the for loop, move dt to be in UTC. Use timezone.utc as a convenient 
  shortcut for UTC.
'''
# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start
  dt = trip['start']
  # Move dt to be in UTC
  dt = dt.astimezone(timezone.utc)

  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())


'''
<script.py> output:
    Original: 2017-10-01 15:23:25-04:00 | UTC: 2017-10-01T19:23:25+00:00
    Original: 2017-10-01 15:42:57-04:00 | UTC: 2017-10-01T19:42:57+00:00
    Original: 2017-10-02 06:37:10-04:00 | UTC: 2017-10-02T10:37:10+00:00
    Original: 2017-10-02 08:56:45-04:00 | UTC: 2017-10-02T12:56:45+00:00
    Original: 2017-10-02 18:23:48-04:00 | UTC: 2017-10-02T22:23:48+00:00
    Original: 2017-10-02 18:48:08-04:00 | UTC: 2017-10-02T22:48:08+00:00
    Original: 2017-10-02 19:18:10-04:00 | UTC: 2017-10-02T23:18:10+00:00
    Original: 2017-10-02 19:37:32-04:00 | UTC: 2017-10-02T23:37:32+00:00
    Original: 2017-10-03 08:24:16-04:00 | UTC: 2017-10-03T12:24:16+00:00
    Original: 2017-10-03 18:17:07-04:00 | UTC: 2017-10-03T22:17:07+00:00
'''
