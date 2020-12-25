'''
01 - Counting missing rows with left join

The Movie Database is supported by volunteers  going  out into  the  world, 
collecting data, and entering it into the database. This includes financial
data, such as movie budget and revenue. If you wanted to know which  movies 
are still missing data, you could use a left join to identify them. Practice 
using a left join by merging the movies table and the financials table.

The movies and financials tables have been loaded for you.

-------------------------------------------------------
movies.head()

      id                 title  popularity release_date
0    257          Oliver Twist   20.415572   2005-09-23
1  14290  Better Luck Tomorrow    3.877036   2002-01-12
2  38365             Grown Ups   38.864027   2010-06-24
3   9672              Infamous    3.680896   2006-11-16
4  12819       Alpha and Omega   12.300789   2010-09-17

financials.head()

       id     budget       revenue
0   19995  237000000  2.787965e+09
1     285  300000000  9.610000e+08
2  206647  245000000  8.806746e+08
3   49026  250000000  1.084939e+09
4   49529  260000000  2.841391e+08

--------------------------------------------------------
Instructions:

1- Question:---------------------------------------------------
What column is likely the best column to merge the two tables on?

Possible Answers
 - on='budget'[X]
 - on='popularity'[X]
 - on='id'[✓]

 2 - Merge the movies table, as the left table, with the financials
     table using a left join, and save the result to movies_financials.

3 - Count the number of rows in movies_financials with a null value in
    the budget column.
'''
# 2--------------------------------------------------------------------
# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# 3--------------------------------------------------------------------

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)
