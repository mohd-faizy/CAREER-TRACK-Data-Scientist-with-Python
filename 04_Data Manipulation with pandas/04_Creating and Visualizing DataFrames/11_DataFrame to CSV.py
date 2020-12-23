'''
11 - DataFrame to CSV
You're almost there! To make things easier to read, you'll need to sort the data
and export it to CSV so that your colleagues can read it.

pandas as pd has been imported for you.

Instructions:

 - Sort airline_totals by the values of bumps_per_10k from highest to lowest, storing 
   as airline_totals_sorted.

 - Print your sorted DataFrame.

 - Save the sorted DataFrame as a CSV called "airline_totals_sorted.csv".
'''
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")