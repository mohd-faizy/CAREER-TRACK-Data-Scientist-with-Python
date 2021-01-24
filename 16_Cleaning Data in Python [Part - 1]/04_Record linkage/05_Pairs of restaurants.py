'''
05 - Pairs of restaurants

In the last lesson, you cleaned the restaurants  dataset to make  it  ready  for 
building a restaurants recommendation engine. You have  a  new  DataFrame  named 
restaurants_new with new restaurants to train your model on, that's been scraped 
from a new data source.

You've already cleaned the cuisine_type and city columns  using  the  techniques
 learned throughout  the  course. However  you  saw  duplicates  with  typos  in 
 restaurants names that require record linkage instead of joins with restaurants.

In this exercise, you will perform the first step in record linkage and generate 
possible pairs of rows between restaurants and restaurants_new. Both DataFrames, 
pandas and recordlinkage are in your environment.

Instructions 1/2

- Instantiate an indexing object by using the Index() function from recordlinkage.
- Block your pairing on cuisine_type by using indexer's' .block() method.
- Generate pairs by indexing restaurants and restaurants_new in that order.
'''
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)


'''
Instructions 2/2

Question:

Now that you've generated your pairs, you've achieved the first step of record linkage. 
What are the steps remaining to link both restaurants DataFrames, and in what order?

Possible Answers

- Compare between columns, score the comparison, then link the DataFrames.[Correct]
- Clean the data, compare between columns, link the DataFrames, then score the comparison.[X]
- Clean the data, compare between columns, score the comparison, then link the DataFrames.[X]
'''
