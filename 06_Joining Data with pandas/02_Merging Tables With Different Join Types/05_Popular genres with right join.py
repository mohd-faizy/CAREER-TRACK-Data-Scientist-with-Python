'''
05 - Popular genres with right join

What  are  the genres of the most popular  movies?  To  answer  this  question, 
you need to  merge  data  from  the  movies  and  movie_to_genres tables. In a 
table called pop_movies, the top 10 most popular movies in  the  movies  table 
have been selected. To ensure  that  you  are  analyzing  all  of  the  popular 
movies, merge it with the movie_to_genres table using a right join. To complete 
your analysis, count the number of different genres. Also, the two tables can be 
merged by the movie ID. However, in pop_movies that column is called id, and in 
movies_to_genres it's called movie_id.

The pop_movies and movie_to_genres tables have been loaded for you.

--------------------------------------------------------------
>pop_movies.head()

          id                    title  popularity release_date
4546  211672                  Minions  875.581305   2015-06-17
4343  157336             Interstellar  724.247784   2014-11-05
1966  293660                 Deadpool  514.569956   2016-02-09
2423  118340  Guardians of the Galaxy  481.098624   2014-07-30
4220   76341       Mad Max: Fury Road  434.278564   2015-05-13

>movie_to_genres.head()

   movie_id            genre
0         5            Crime
1         5           Comedy
2        11  Science Fiction
3        11           Action
4        11        Adventure

--------------------------------------------------------------
Instructions:

- Merge movie_to_genres and pop_movies using a right join. Save the results as genres_movies.
- Group genres_movies by genre and count the number of id values.
'''
# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right',
                                      left_on='movie_id',
                                      right_on='id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id': 'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()
