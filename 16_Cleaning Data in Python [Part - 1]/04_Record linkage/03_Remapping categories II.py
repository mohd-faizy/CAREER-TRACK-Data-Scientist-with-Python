'''
03 - Remapping categories II

In the last exercise, you determined that the distance cutoff  point  for  remapping 
typos of 'american', 'asian', and 'italian' cuisine types stored in the cuisine_type 
column should be 80.

In this exercise, you're going to put it all together by finding  matches  with  similarity
scores equal to or higher than 80 by  using `fuzywuzzy.process's` `extract()` function, for 
each correct cuisine type, and replacing these matches with  it. Remember,  when  comparing 
a string with an array of strings using `process.extract()`, the output is a list of tuples 
where each of tuple is as such:
-----------------------------------------------------------------
`(closest match, similarity score, index of match)`
-----------------------------------------------------------------

The restaurants DataFrame is in your environment, and you have access to a categories 
list containing the correct cuisine types ('italian', 'asian', and 'american').

Instructions 1/4

- Using the method shown in the video, return all of the unique values for the cuisine_type 
  column of restaurants.

'''
# Inspect the unique values of the cuisine_type column
print(restaurants['cuisine_type'].unique())


'''
Instructions 2/4

Okay! Looks like you will need to use some string matching to correct these misspellings!

    - As a first step, create a list of matches comparing 'italian' with the restaurant 
      types listed in the cuisine_type column.

    - Inspect the first five elements of matches. This has been done for you.
'''
# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract(
    'italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type)
    )

# Inspect the first 5 matches
print(matches[0:5])

'''
Instructions 3/4

Now you're getting somewhere! Now you can iterate through matches to reassign similar entries.

    - Within the for loop, use an if statement to check whether the similarity score in each 
      match is greater than or equal to 80.

    - If it is, use .loc to select rows where cusine_type in restaurants is equal to the current 
      match (which is the first element of match), and reassign them to be 'italian'.
'''
# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract(
    'italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Iterate through the list of matches to italian
for match in matches:
  # Check whether the similarity score is greater than or equal to 80
  if match[1] >= 80:
    # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
    restaurants.loc[restaurants['cuisine_type'] == match[0]] = 'italian'


'''
Instructions 4/4

Finally, you'll adapt your code to work with every restaurant type in categories.

    - Using the variable cuisine to iterate through categories, embed your code from the 
      previous step in an outer for loop.
      
    - Inspect the final result. This has been done for you.
'''
# Iterate through categories
for cuisine in categories:
  # Create a list of matches, comparing cuisine with the cuisine_type column
  matches = process.extract(
      cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

  # Iterate through the list of matches
  for match in matches:
     # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
      restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine

# Inspect the final result
restaurants['cuisine_type'].unique()
