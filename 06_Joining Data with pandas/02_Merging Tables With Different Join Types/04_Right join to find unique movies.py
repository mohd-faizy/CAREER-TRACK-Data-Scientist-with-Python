'''
05 - Right join to find unique movies

Most of  the  recent  big-budget  science  fiction  movies  can  also  be  classified 
as action movies. You are given a table  of science fiction movies called scifi_movies
and another table of action movies  called action_movies. Your goal is to  find  which 
movies are considered only science fiction movies. Once you  have this table, you  can 
merge the movies table in to see the movie names. Since this exercise  is  related  to 
science fiction movies, use a right join as your superhero power to solve this problem.

The movies, scifi_movies, and action_movies tables have been loaded for you.

-------------------------------------------------------------
> movies.head()

      id                 title  popularity release_date
0    257          Oliver Twist   20.415572   2005-09-23
1  14290  Better Luck Tomorrow    3.877036   2002-01-12
2  38365             Grown Ups   38.864027   2010-06-24
3   9672              Infamous    3.680896   2006-11-16
4  12819       Alpha and Omega   12.300789   2010-09-17

> scifi_movies.head()

    movie_id            genre
2         11  Science Fiction
17        18  Science Fiction
20        19  Science Fiction
38        38  Science Fiction
49        62  Science Fiction

> action_movies.head()

    movie_id   genre
3         11  Action
14        18  Action
25        22  Action
26        24  Action
42        58  Action

-------------------------------------------------------------
Instructions:

1. Merge action_movies and scifi_movies tables with a right join on movie_id. Save the result
   as action_scifi.


2. Update the merge to add suffixes, where '_act' and '_sci' are suffixes for the left and right
   tables, respectively.

3. From action_scifi, subset only the rows where the genre_act column is null.

4. Merge movies and scifi_only using the id column in the left table and the movie_id column in
   the right table with an inner join.
'''
# 1--------------------------------------------------
# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right')

# 2--------------------------------------------------
# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())

# 3--------------------------------------------------
# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# 4--------------------------------------------------
# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act', '_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, how='inner',
                                     left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)
