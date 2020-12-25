'''
02 - Enriching a dataset

Setting how='left' with the .merge()method is a useful technique for enriching
or enhancing a dataset with additional information from  a  different table. In 
this exercise, you will start off with a sample of movie  data  from  the movie
series Toy Story. Your goal is to enrich this data by adding the  marketing tag
line for each movie. You will compare the results of a left join versus an inner
join.

The toy_story DataFrame contains the Toy Story movies. The toy_story and taglines
DataFrames have been loaded for you.

--------------------------------------------------------
toy_story.head()

      id        title  popularity release_date
0  10193  Toy Story 3   59.995418   2010-06-16
1    863  Toy Story 2   73.575118   1999-10-30
2    862    Toy Story   73.640445   1995-10-30

taglines.head()

       id                                         tagline
0   19995                     Enter the World of Pandora.
1     285  At the end of the world, the adventure begins.
2  206647                           A Plan No One Escapes
3   49026                                 The Legend Ends
4   49529            Lost in our world, found in another.

--------------------------------------------------------

Instructions:

1. Merge toy_story and taglines on the id column with a left join, and save the result
   as toystory_tag.

2. With toy_story as the left table, merge to it taglines on the id column with an inner
   join, and save as toystory_tag
'''
# 1---------------------------------------------------------
# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# 2---------------------------------------------------------
# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on='id', how='inner')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

