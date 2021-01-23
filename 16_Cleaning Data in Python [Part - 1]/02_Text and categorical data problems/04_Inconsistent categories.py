'''
4 - Inconsistent categories:

In this exercise, you'll be revisiting the airlines DataFrame from the 
previous lesson.

As a reminder, the DataFrame contains flight metadata such as  the  airline, 
the destination, waiting times as well as answers to key questions regarding 
cleanliness, safety, and satisfaction on the San Francisco Airport.

In this exercise, you will examine two categorical columns from this DataFrame, 
dest_region and dest_size respectively, assess how to address them and make sure 
that they are cleaned and ready for analysis. The pandas package has been imported
as pd, and the airlines DataFrame is in your environment.

----------------------------------------------------------------------------------------------
Instructions 1/4
----------------------------------------------------------------------------------------------
- Print the unique values in dest_region and dest_size respectively.
'''
# importing pandas
import pandas as pd

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

'''
<script.py> output:

    ['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
     'Middle East' 'Europe' 'eur' 'Central/South America'
     'Australia/New Zealand' 'middle east']

    ['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
     'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
'''

'''
----------------------------------------------------------------------------------------------
Instructions 2/4
----------------------------------------------------------------------------------------------
Question:

From looking at the output, what do you think is the problem with these columns?

Possible Answers
- The dest_region column has only inconsistent values due to capitalization.[X]
- The dest_region column has inconsistent values due to capitalization and has one 
  value that needs to be remapped.[X]
- The dest_size column has only inconsistent values due to leading and trailing spaces.[X]
- Both 2 and 3 are correct.[Correct]
'''

'''
----------------------------------------------------------------------------------------------
Instructions 3/4
----------------------------------------------------------------------------------------------
- Change the capitalization of all values of dest_region to lowercase.
- Replace the 'eur' with 'europe' in dest_region using the .replace() method.
'''
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur': 'europe'})

'''
----------------------------------------------------------------------------------------------
Instructions 4/4
----------------------------------------------------------------------------------------------
- Strip white spaces from the dest_size column using the .strip() method.
- Verify that the changes have been into effect by printing the unique values 
  of the columns using .unique() .
 
'''
# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur': 'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

'''
<script.py> output:
    ['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
     'Middle East' 'Europe' 'eur' 'Central/South America'
     'Australia/New Zealand' 'middle east']
    ['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
     'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
    ['asia' 'canada/mexico' 'west us' 'east us' 'midwest us' 'middle east'
     'europe' 'central/south america' 'australia/new zealand']
    ['Hub' 'Small' 'Medium' 'Large']
'''
