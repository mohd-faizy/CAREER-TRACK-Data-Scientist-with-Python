'''
10 - CSV to DataFrame:

You  work for  an  airline,  and  your  manager has  asked  you  to  do  a  competitive
analysis  and see  how often  passengers flying  on  other  airlines  are  involuntarily
bumped from their flights. You got a CSV file (airline_bumping.csv) from the Department 
of Transportation containing data on passengers that were involuntarily denied boarding 
in 2016 and 2017, but it doesn't have the exact numbers you want. In order to figure this 
out, you'll need to get the CSV into a pandas DataFrame and do some manipulation!

pandas is imported for you as pd. "airline_bumping.csv" is in your working directory.

Instructions:

-1--------------------------------------------------------------------------------------------
- Read the CSV file "airline_bumping.csv" and store it as a DataFrame called airline_bumping.

- Print the first few rows of airline_bumping.
'''
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping.head())


'''
-2--------------------------------------------------------------------------------------------
- For each airline group, select the nb_bumped, and total_passengers columns, and calculate the
  sum (for both years). Store this as airline_totals.
'''
# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

'''
-3---------------------------------------------------------------------------------------------
- Create a new column of airline_totals called bumps_per_10k, which is the number of passengers 
  bumped per 10,000 passengers in 2016 and 2017.
'''
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000


'''
-4---------------------------------------------------------------------------------------------
- Print airline_totals to see the results of your manipulations.
'''
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)
