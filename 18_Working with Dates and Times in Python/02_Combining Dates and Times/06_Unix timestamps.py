'''
06 - Unix timestamps

Datetimes are sometimes stored as Unix timestamps: the  number of  seconds  since 
January 1, 1970. This is especially common with computer infrastructure, like the 
log files that websites keep when they get visitors.

Instructions

- Complete the for loop to loop over timestamps.
- Complete the code to turn each timestamp ts into a datetime.
'''
# Import datetime
from datetime import datetime

# Starting timestamps
timestamps = [1514665153, 1514664543]

# Datetime objects
dts = []

# Loop
for ts in timestamps:
  dts.append(datetime.fromtimestamp(ts))

# Print results
print(dts)

'''
<script.py> output:
    [datetime.datetime(2017, 12, 30, 20, 19, 13), datetime.datetime(2017, 12, 30, 20, 9, 3)]

The largest number that some older computers can hold in one variable is 2147483648, which as
a Unix timestamp is in January 2038. On that day, many computers which haven't been upgraded 
will fail.
'''
