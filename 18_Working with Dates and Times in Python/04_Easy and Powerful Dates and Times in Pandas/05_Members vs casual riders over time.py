'''
05 - Members vs casual riders over time

Riders can either be "Members", meaning they pay yearly for the ability 
to take a bike at any time, or "Casual", meaning they pay at the  kiosk 
attached to the bike dock.

Do members and casual riders drop off at the same rate over October to 
December, or does one drop off faster than the other?

As before, rides has been loaded for you. You're going to  use  the  Pandas 
method .value_counts(), which returns the number of instances of each value 
in a Series. In this case, the counts of "Member" or "Casual".

Instructions

- Set monthly_rides to be a resampled version of rides, by month, based on 
  start date.
- Use the method .value_counts() to find out how many Member and Casual rides 
  there were, and divide them by the total number of rides per month.
'''
# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())


'''
<script.py> output:
    Start date  Member type
    2017-10-31  Member         0.768519
                Casual         0.231481
    2017-11-30  Member         0.825243
                Casual         0.174757
    2017-12-31  Member         0.860759
                Casual         0.139241
    Name: Member type, dtype: float64
'''
