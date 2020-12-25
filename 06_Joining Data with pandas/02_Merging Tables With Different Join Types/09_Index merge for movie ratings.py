'''
09 - Index merge for movie ratings

To practice merging on indexes, you will merge movies  and a  table  called 
ratings that holds info about movie ratings. Make sure your  merge  returns 
all of the rows from the movies table and not all the rows of ratings table
need to be included in the result.

The movies and ratings tables have been loaded for you.
----------------------------------------------------
movies.head()

                      title  popularity release_date
id                                                  
257            Oliver Twist   20.415572   2005-09-23
14290  Better Luck Tomorrow    3.877036   2002-01-12
38365             Grown Ups   38.864027   2010-06-24
9672               Infamous    3.680896   2006-11-16
12819       Alpha and Omega   12.300789   2010-09-17

ratings.head()

        vote_average  vote_count
id                              
19995            7.2     11800.0
285              6.9      4500.0
206647           6.3      4466.0
49026            7.6      9106.0
49529            6.1      2124.0
----------------------------------------------------

Instructions

- Merge movies and ratings on the index and save to a variable called movies_ratings,
  ensuring that all of the rows from the movies table are returned.
'''
# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())
