'''
08 - Concatenate and merge to find common songs

The senior leadership of the streaming  service is  requesting  your  help  again. 
You are given the historical files for a popular playlist in the  classical  music
genre in 2018 and 2019. Additionally, you are given a similar set of files for the
most popular pop music genre playlist on the streaming service in 2018 and 2019. 

Your goal is to concatenate the respective files to make a large classical  playlist 
table and overall popular music table. Then filter the classical music table using a 
semi-join to return only the most popular classical music tracks.

The tables classic_18, classic_19, and pop_18, pop_19 have been loaded for you. Additionally, pandas has been loaded as pd.

-----------------------
classic_18.head()
-----------------------
      pid   tid
8527   12  3483
8586   12  3416
8533   12  3489
8523   12  3479
8558   12  3440

-----------------------
classic_19.head()
-----------------------
      pid   tid
8526   12  3482
8552   12  3434
8566   12  3448
8543   12  3499
8595   12  3425

-----------------------
pop_18.head()
-----------------------

      pid   tid
3150    1  3063
315     1  2712
2178    1  2641
2772    1  2271
430     1   919

-----------------------
pop_19.head()
-----------------------
      pid   tid
2639    1  2115
1867    1   297
910     1   272
3107    1  3023
723     1  1193

Instructions 1/2:

- Concatenate the classic_18 and classic_19 tables vertically where the index goes
  from 0 to n-1, and save to classic_18_19.

- Concatenate the pop_18 and pop_19 tables vertically where the index goes from 0 
  to n-1, and save to pop_18_19.
'''
# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)


'''
Instructions 2/2:

- With classic_18_19 on the left, merge it with pop_18_19 on tid using an inner join.
- Use .isin() to filter classic_18_19 where tid is in classic_pop.
'''
# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)