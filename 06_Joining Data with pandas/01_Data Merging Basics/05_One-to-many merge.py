'''
05 - One-to-many merge

A business may have one  or  multiple  owners. In  this  exercise,  you  will 
continue  to  gain  experience  with  one-to-many  merges  by merging a table 
of business owners, called biz_owners,  to  the  licenses  table. Recall from 
the video lesson, with a one-to-many relationship, a row in  the  left  table 
may be repeated if it is related to multiple rows in the right table. In this 
lesson, you will explore this further by finding out what is the most  common 
business owner title. (i.e., secretary, CEO, or vice president)

The licenses and biz_owners DataFrames are loaded for you.

Instructions:

- Starting with the licenses table on the left, merge it to the biz_owners table
  on the column account, and save the results to a variable named licenses_owners.

- Group licenses_owners by title and count the number of accounts for each title. 
  Save the result as counted_df.

- Sort counted_df by the number of accounts in descending order, and save this as a
  variable named sorted_df.

- Use the .head() method to print the first few rows of the sorted_df

-----------------------------------------------------------------------------------
licenses.head()

  account ward  aid                   business               address    zip
0  307071    3  743       REGGIE'S BAR & GRILL       2105 S STATE ST  60616
1      10   10  829                 HONEYBEERS   13200 S HOUSTON AVE  60633
2   10002   14  775                CELINA DELI     5089 S ARCHER AVE  60632
3   10005   12  NaN  KRAFT FOODS NORTH AMERICA        2005 W 43RD ST  60609
4   10044   44  638  NEYBOUR'S TAVERN & GRILLE  3651 N SOUTHPORT AVE  60613


biz_owners.head()

  account first_name  last_name      title
0      10      PEARL    SHERMAN  PRESIDENT
1      10      PEARL    SHERMAN  SECRETARY
2   10002     WALTER     MROZEK    PARTNER
3   10002     CELINA     BYRDAK    PARTNER
4   10005      IRENE  ROSENFELD  PRESIDENT
-----------------------------------------------------------------------------------
'''
# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account': 'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by='account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

