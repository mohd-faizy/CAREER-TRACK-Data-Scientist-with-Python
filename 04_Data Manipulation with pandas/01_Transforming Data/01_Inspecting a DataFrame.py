'''
01 - Inspecting a DataFrame

When you get a new DataFrame to work with, the first thing you need to do is explore it
and see what it contains.There are several useful methods and attributes for this.

 - .head() returns the first few rows (the “head” of the DataFrame).

 - .info() shows information on each of the columns, such as the data type and number
   of missing values.

 - .shape returns the number of rows and columns of the DataFrame.

 - .describe() calculates a few summary statistics for each column.

homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018.
The individual column is the number of homeless individuals not part of a family with children.
The family_members column is the number of homeless individuals part of a family with children.
The state_pop column is the state's total population.

Instructions:
 
 - Print the head(), info(), shape & .describe() of the homelessness DataFrame.

'''
import pandas as pd

homelessness = pd.read_csv('content/homelessness.csv')

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())
