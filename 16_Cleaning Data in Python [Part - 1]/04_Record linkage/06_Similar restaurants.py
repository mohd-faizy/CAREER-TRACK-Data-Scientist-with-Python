'''
06 - Similar restaurants

In the last exercise, you generated pairs  between  restaurants  and 
restaurants_new in an effort to cleanly merge both  DataFrames using 
record linkage.

When performing record linkage, there are different types  of  matching 
you can perform between different columns of your DataFrames, including 
`exact` matches, `string` similarities, and more.

Now that your pairs have been generated and  stored  in  pairs,  you  will 
find exact matches in the city and cuisine_type columns between each  pair, 
and similar strings for each pair in the rest_name column. Both DataFrames, 
pandas and recordlinkage are in your environment.

Instructions:

- Instantiate a comparison object using the recordlinkage.Compare() function.
- Use the appropriate comp_cl method to find exact matches between the city 
  and cuisine_type columns of both DataFrames.
- Use the appropriate comp_cl method to find similar strings with a 0.8 similarity 
  threshold in the rest_name column of both DataFrames.
- Compute the comparison of the pairs by using the .compute() method of comp_cl.
'''
# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types -
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold=0.8)

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)



'''
Question:

Print out potential_matches, the columns are the columns being  compared, 
with values being 1 for a match, and 0 for not a match for each pair  of 
rows in your DataFrames. To find potential matches, you need to find rows 
with more than matching value in a column. You can find them with

-------------------------------------------------------
potential_matches[potential_matches.sum(axis = 1) >= n]
-------------------------------------------------------

Where n is the minimum number of columns you want matching to ensure a proper 
duplicate find, what do you think should the value of n be?

Possible Answers

- 3 because I need to have matches in all my columns.[Correct]

- 2 because matching on any of the 2 columns or more is enough to find potential 
  duplicates.[X]

- 1 because matching on just 1 column like the restaurant name is enough to find 
  potential duplicates.[X]
'''
