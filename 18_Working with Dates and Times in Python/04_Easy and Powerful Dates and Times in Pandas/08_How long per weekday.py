'''
08 - How long per weekday?

Pandas has a number of datetime-related  attributes  within the 
.dt accessor. Many of them are ones you've encountered  before, 
like .dt.month. Others are convenient and save time compared to 
standard Python, like .dt.weekday_name.

Instructions

- Add a new column to rides called 'Ride start weekday', which is the 
  weekday of the Start date.

- Print the median ride duration for each weekday.
'''
# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())

'''
Output:
-------------------------------
Ride start weekday
Friday       724.5
Monday       810.5
Saturday     462.0
Sunday       902.5
Thursday     652.0
Tuesday      641.5
Wednesday    585.0
Name: Duration, dtype: float64
-------------------------------

There are .dt attributes for all of the common things you might  want  to  pull 
out of a datetime, such as the day, month, year, hour, and so on, and also some 
additional convenience ones, such as quarter and week of the year out of 52.
'''
