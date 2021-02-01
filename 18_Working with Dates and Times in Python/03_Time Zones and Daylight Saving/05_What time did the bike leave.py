'''
05 - What time did the bike leave? (Global edition)

When you need to move a datetime from one  timezone  into  another,  use 
.astimezone() and tz. Often you will be moving things into UTC, but  for 
fun let's try moving things from 'America/New_York' into a few different 
time zones.
------------------------------------------------------------------
Instructions:

- Set uk to be the timezone for the UK: 'Europe/London'.
- Change local to be in the uk timezone and assign it to notlocal.
------------------------------------------------------------------
'''
# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

'''
<script.py> output:
    2017-10-01T15:23:25-04:00
    2017-10-01T20:23:25+01:00
'''

'''
------------------------------------------------------------------
- Set ist to be the timezone for India: 'Asia/Kolkata'.
- Change local to be in the ist timezone and assign it to notlocal.
------------------------------------------------------------------
'''
# Create the timezone object
ist = tz.gettz('Asia/Kolkata')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(ist)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

'''
<script.py> output:
    2017-10-01T15:23:25-04:00
    2017-10-02T00:53:25+05:30
'''

'''
------------------------------------------------------------------
- Set sm to be the timezone for Samoa: 'Pacific/Apia'.
- Change local to be in the sm timezone and assign it to notlocal.
------------------------------------------------------------------
'''
# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

'''
<script.py> output:
    2017-10-01T15:23:25-04:00
    2017-10-02T09:23:25+14:00
'''
