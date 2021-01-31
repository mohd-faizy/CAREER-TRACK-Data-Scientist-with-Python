'''
08 - Average trip time

W20529 took 291 trips in our data set. How long were the trips on average? We can 
use the built-in Python functions sum() and len() to make this calculation.

Based on your last coding exercise, the data has been loaded as onebike_durations. 
Each entry is a number of seconds that the bike was out of the dock.

Instructions

- Calculate total_elapsed_time across all trips in onebike_durations.
- Calculate number_of_trips for onebike_durations.
- Divide total_elapsed_time by number_of_trips to get the average trip length.
'''
# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)

# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)

'''
For the average to be a helpful summary of the data, we need for all of our durations to 
be reasonable numbers, and not a few that are way too big, way too small, or even malformed. 
For example, if there is anything fishy happening in the data, and our trip ended before it 
started, we'd have a negative trip length.
'''
