'''
10- Do sequels earn more?

It is time to put together  many  of the  aspects  that  you  have  learned  in 
this  chapter. In  this  exercise, you'll find out  which movie  sequels  earned 
the most compared to the  original  movie. To  answer  this  question, you  will 
merge a modified version of  the  sequels  and  financials  tables  where  their 
index is the movie ID. You will need to choose a merge  type  that  will  return
all of the rows from the sequels table  and  not  all  the  rows  of  financials 
table need to be included in the result. From there, you will join the resulting
table to itself so that you can compare the revenue values of the original movie
to the sequel. Next, you will calculate the difference between the two revenues
and sort the resulting dataset.

The sequels and financials tables have been provided.

-------------------------------
sequels.head()

              title sequel
id                        
19995        Avatar    nan
862       Toy Story    863
863     Toy Story 2  10193
597         Titanic    nan
24428  The Avengers    nan

financials.head()

           budget       revenue
id                             
19995   237000000  2.787965e+09
285     300000000  9.610000e+08
206647  245000000  8.806746e+08
49026   250000000  1.084939e+09
49529   260000000  2.841391e+08
-------------------------------
Instructions:
-------------------------------------------------------------------------------------
1. With the sequels table on the left, merge to it the financials  table  on  index
   named id, ensuring that all the rows from the sequels are returned and some rows
   from the other table may not be returned, Save the results to sequels_fin.
'''
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

'''
-------------------------------------------------------------------------------------
2. Merge the sequels_fin table to itself with an inner join, where the left and right 
   tables merge on sequel and id respectively with suffixes equal to ('_org','_seq'), 
   saving to orig_seq.
'''
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

'''
-------------------------------------------------------------------------------------
3. Select the title_org, title_seq, and diff columns of orig_seq and save this as titles_diff.
'''
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

'''
-------------------------------------------------------------------------------------
4. Sort by titles_diff by diff in descending order and print the first few rows.
'''
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending=False).head())