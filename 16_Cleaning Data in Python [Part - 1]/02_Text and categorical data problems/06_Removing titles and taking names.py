'''
06 - Removing titles and taking names

While collecting survey respondent metadata in the airlines DataFrame,
the full name of respondents was saved in the full_name column. However 
upon closer inspection, you found that a lot of the different names are 
prefixed by honorifics such as "Dr.", "Mr.", "Ms." and "Miss".

Your ultimate objective is to create two new columns named first_name and 
last_name, containing the first and last names of respondents respectively. 
Before doing so however, you need to remove honorifics.

The airlines DataFrame is in your environment, alongside pandas as pd.

Instructions:

- Remove "Dr.", "Mr.", "Miss" and "Ms." from full_name by replacing them with 
  an empty string "" in that order.
- Run the assert statement using .str.contains() that tests whether full_name 
  still contains any of the honorifics.
'''
# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.", "")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False
