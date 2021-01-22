'''
01 - Numeric data or ... ?

In this exercise, and throughout this chapter, you'll be working with bicycle ride 
sharing data in San Francisco called ride_sharing. It contains information  on  the 
start and end stations, the trip duration, and some user information for a bike 
sharing service.

The `user_type` column contains information on whether a user is taking a free ride and 
takes on the following values:

    1 - for free riders.
    2 - for pay per ride.
    3 - for monthly subscribers.

In this instance, you will print the information of ride_sharing using .info() and see 
a firsthand example of how an incorrect data type can flaw your analysis of the dataset. 
The pandas package is imported as pd.

Instructions 1/3

- Print the information of ride_sharing.
- Use .describe() to print the summary statistics of the `user_type` column from ride_sharing.
'''
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 25760 entries, 0 to 25759
Data columns (total 9 columns):
duration           25760 non-null object
station_A_id       25760 non-null int64
station_A_name     25760 non-null object
station_B_id       25760 non-null int64
station_B_name     25760 non-null object
bike_id            25760 non-null int64
user_type          25760 non-null int64
user_birth_year    25760 non-null int64
user_gender        25760 non-null object
dtypes: int64(5), object(4)
memory usage: 2.0+ MB
None
count    25760.000000
mean         2.008385
std          0.704541
min          1.000000
25%          2.000000
50%          2.000000
75%          3.000000
max          3.000000
Name: user_type, dtype: float64
'''
'''
Instructions 2/3

Question:
By looking at the summary statistics - they don't really seem to offer much description 
on how users are distributed along their purchase type, why do you think that is?

Possible Answers

- The `user_type` column is not of the correct type, it should be converted to str.[X]

- The `user_type` column has an infinite set of possible values, it should be converted
  to category.[X]

- The `user_type` column has an finite set of possible values that represent groupings of
  data, it should be converted to category.[Correct]
'''

'''
Instructions 3/3

- Convert user_type into categorical by assigning it the 'category' data type and store it in the
  user_type_cat column.
- Make sure you converted user_type_cat correctly by using an assert statement.
'''
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics
print(ride_sharing['user_type_cat'].describe())

'''
Name: user_type, dtype: float64
count     25760
unique        3
top           2
freq      12972
Name: user_type_cat, dtype: int64
'''