'''
02 - Counting events before and after noon

In this chapter, you will be working with a list of all bike trips  for  one  Capital 
Bikeshare bike, W20529, from October 1, 2017 to December 31, 2017. This list has been 
loaded as onebike_datetimes.

Each element of the list is a dictionary with two entries: start is a datetime object 
corresponding to the start of a trip (when a bike is removed from the dock) and end is 
a datetime object corresponding to the end of a trip (when a bike is put back into a 
dock).

You can use this data set to understand better how this bike was used. Did more trips 
start before noon or after noon?

Instructions:

- Within the for loop, complete the if statement to check if the trip started before noon.
- Within the for loop, increment trip_counts['AM'] if the trip started before noon, and 
  trip_counts['PM'] if it started after noon.
'''
#import pandas as pd
#from datetime import date
#df = pd.read_csv('../file.csv')

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for trip in onebike_datetimes:
  # Check to see if the trip starts before noon
  if trip['start'].hour < 12:
    # Increment the counter for before noon
    trip_counts['AM'] += 1
  else:
    # Increment the counter for after noon
    trip_counts['PM'] += 1

print(trip_counts)

'''
<script.py> output:
    {'AM': 94, 'PM': 196}

It looks like this bike is used about twice as much after noon 
than it is before noon. One obvious follow up would be to see which 
hours the bike is most likely to be taken out for a ride.
'''
