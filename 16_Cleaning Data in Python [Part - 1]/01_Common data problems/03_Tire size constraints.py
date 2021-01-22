'''
03 - Tire size constraints

In this lesson, you're going to build on top of the work you've been doing 
with the ride_sharing DataFrame. You'll be working with the tire_sizes 
column which contains data on each bike's tire size.

Bicycle tire sizes could be either 26″, 27″ or 29″ and are here correctly 
stored as a categorical value. In an effort to cut maintenance costs, the 
ride sharing provider decided to set the maximum tire size to be 27″.

In this exercise, you will make sure the tire_sizes column has the correct 
range by first converting it to an integer, then setting and testing the new 
upper limit of 27″ for tire sizes.

Instructions

- Convert the tire_sizes column from category to 'int'.
- Use .loc[] to set all values of tire_sizes above 27 to 27.
- Reconvert back tire_sizes to 'category' from int.
- Print the description of the tire_sizes.
'''
# import pandas
import pandas as pd

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

'''
count     25760
unique        2
top          27
freq      13274
Name: tire_sizes, dtype: int64

<script.py> output:
    count     25760
    unique        2
    top          27
    freq      13274
    Name: tire_sizes, dtype: int64
'''
