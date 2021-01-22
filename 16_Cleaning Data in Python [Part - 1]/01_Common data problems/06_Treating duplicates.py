'''
06 - Treating duplicates

In the last exercise, you  were able  to verify that the  new  update 
feeding into ride_sharing  contains a bug  generating  both  complete 
and incomplete duplicated rows for some values of the ride_id  column, 
with occasional discrepant values for the user_birth_year and duration 
columns.

In this exercise, you will be treating those duplicated rows  by  first 
dropping complete duplicates, and then merging the incomplete duplicate 
rows into one while keeping  the  average  duration,  and  the  minimum 
user_birth_year for each set of incomplete duplicate rows.

Instructions

- Drop complete duplicates in ride_sharing and store the results in ride_dup.
- Create the statistics dictionary which holds minimum aggregation for 
  user_birth_year and mean aggregation for duration.
- Drop incomplete duplicates by grouping by ride_id and applying the aggregation
  in statistics.
- Find duplicates again and run the assert statement to verify de-duplication.
'''
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
