'''
04 - Back to the future

A new update to the data pipeline feeding into the ride_sharing DataFrame has 
been updated to register each ride's date. This information is stored in  the 
ride_date column of the type object, which represents strings in pandas.

A bug was discovered which was relaying rides taken today as taken next year. 
To fix this, you will find all instances of the ride_date  column  that occur 
anytime in the future, and set the maximum possible value of this column to today's 
date. Before doing so, you would need to convert ride_date to a datetime object.

The datetime package has been imported as dt, alongside all the packages you've 
been using till now.

Instructions

- Convert ride_date to a datetime object and store it in ride_dt column using to_datetime().
- Create the variable today, which stores today's date by using the dt.date.today() function.
- For all instances of ride_dt in the future, set them to today's date.
- Print the maximum date in the ride_dt column.
'''
import datetime as dt
import pandas as pd

# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

'''
<script.py> output:
    2021-01-22 00:00:00
'''
