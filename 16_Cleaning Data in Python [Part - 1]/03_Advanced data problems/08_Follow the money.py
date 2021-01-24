'''
08 - Follow the money

In this exercise, you're working with another version of the banking DataFrame that 
contains missing values for both the cust_id column and the acct_amount column.

You want to produce analysis on how many unique customers the  bank  has,  the  average 
amount held by customers and more. You know that rows with missing cust_id don't really 
help you, and that on average acct_amount is usually 5 times the amount of inv_amount.

In this exercise, you will drop rows of banking with missing cust_ids, and impute missing 
values of acct_amount with some domain knowledge.

Instructions:

- Use .dropna() to drop missing values of the cust_id column in banking and store the 
  results in banking_fullid.

- Compute the estimated acct_amount of banking_fullid knowing that acct_amount is usually 
  inv_amount * 5 and assign the results to acct_imp.

- Impute the missing values of acct_amount in banking_fullid with the newly created acct_imp 
  using .fillna().
'''

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())

'''
<script.py> output:
    cust_id             0
    acct_amount         0
    inv_amount          0
    account_opened      0
    last_transaction    0
    dtype: int64
'''
