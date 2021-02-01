'''
01 - Loading a csv file in Pandas

The capital_onebike.csv file covers the October, November and December 
rides of the Capital Bikeshare bike W20529.

Here are the first two columns:
____________________________________________
Start date	End date	...
____________________________________________
2017-10-01 15:23:25	2017-10-01 15:26:26	...
____________________________________________
2017-10-01 15:42:57	2017-10-01 17:49:59	...
____________________________________________

Instructions:

- Import Pandas.
- Complete the call to read_csv() so that it correctly parses the date columns 
  Start date and End date.
'''
# Import pandas
import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])


'''
<script.py> output:
    Start date                        2017-10-01 15:23:25
    End date                          2017-10-01 15:26:26
    Start station number                            31038
    Start station                    Glebe Rd & 11th St N
    End station number                              31036
    End station             George Mason Dr & Wilson Blvd
    Bike number                                    W20529
    Member type                                    Member
    Name: 0, dtype: object
'''
