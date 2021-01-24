'''
02 - Uniform currencies

In this exercise and throughout this chapter, you  will be  working  with  a  retail 
banking dataset stored in the banking DataFrame. The dataset contains  data  on  the 
amount of money stored in accounts, their currency, amount invested, account opening 
date and last transaction date that were consolidated from American and European 
branches.

You are tasked with understanding the average account size and how investments vary by 
the size of account, however in order to produce this analysis accurately, you first need
to unify the currency amount into dollars. The pandas package has been imported as pd, 
and the banking DataFrame is in your environment.

Instructions

- Find the rows of acct_cur in banking that are equal to 'euro' and store them in acct_eu.
- Find all the rows of acct_amount in banking that fit the acct_eu condition, and convert them
  to USD by multiplying them with 1.1.
- Find all the rows of acct_cur in banking that fit the acct_eu condition, set them to 'dollar'.

'''
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'
