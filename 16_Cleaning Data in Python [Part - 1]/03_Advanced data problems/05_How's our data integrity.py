'''
05 - How's our data integrity?

New data has been merged into the banking DataFrame that contains details on 
how investments in the inv_amount column are allocated across four different 
funds A, B, C and D.

Furthermore, the age and birthdays of customers are now stored in the age and 
birth_date columns respectively.

You want to understand how customers of different age groups  invest. However, 
you want to first make sure the data you're analyzing is correct. You will do 
so by cross field checking values of inv_amount  and  age  against the  amount 
invested in different funds and customers' birthdays. Both pandas and datetime 
have been imported as pd and dt respectively.
-----------------------------------------------------------------------------------------
Instructions 1/2
-----------------------------------------------------------------------------------------
- Find the rows where the sum of all rows of the `fund_columns` in banking are equal 
  to the `inv_amount` column.
- Store the values of banking with consistent inv_amount in consistent_inv, and those
  with inconsistent ones in inconsistent_inv.
'''
# importing the libraries
import datetime as dt
import pandas as pd

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

# OUTPUT:- Number of inconsistent investments:  8
'''
-----------------------------------------------------------------------------------------
Instructions 2/2
-----------------------------------------------------------------------------------------
- Store today's date into today, and manually calculate customers' ages and store them 
  in ages_manual.
- Find all rows of banking where the age column is equal to ages_manual and then filter 
  banking into consistent_ages and inconsistent_ages.
'''
# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])

# OUTPUT: Number of inconsistent ages:  4
