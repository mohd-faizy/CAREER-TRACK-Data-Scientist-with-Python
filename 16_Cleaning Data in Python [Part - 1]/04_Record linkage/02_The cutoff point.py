'''
02 - The cutoff point

In this exercise, and throughout this chapter, you'll be working  with  the 
restaurants DataFrame which has data on various restaurants. Your  ultimate 
goal is to create a restaurant recommendation engine, but you need to first 
clean your data.

This version of restaurants has been collected  from many  sources, where  the 
cuisine_type column is riddled  with typos, and  should contain  only  italian, 
american and asian cuisine types. There are  so  many  unique categories  that 
remapping them manually isn't scalable, and it's best to use string similarity 
instead.

Before doing so, you want to establish the cutoff point for the similarity  score 
using the fuzzywuzzy's process.extract() function by finding the similarity score 
of the most distant typo of each category.

Instructions 1/2

- Import process from fuzzywuzzy.
- Store the unique cuisine_types into unique_types.
- Calculate the similarity of 'asian', 'american', and 'italian' to all possible 
  cuisine_types using process.extract(), while returning all possible matches.

----------------------------------------------
restaurants.head()

                    rest_name  ... cuisine_type
0  arnie morton  s of chicago  ...      america
1         art  s delicatessen  ...      merican
2                   campanile  ...     amurican
3                       fenix  ...     americen
4          grill on the alley  ...    americann

[5 rows x 5 columns]
----------------------------------------------
'''
# Import process from fuzzywuzzy
from fuzzywuzzy import process

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit=len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit=len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit=len(unique_types)))


'''
<script.py> output:
    [('asian', 100), ('asiane', 91), ('asiann', 91), ('asiian', 91), ('asiaan', 91), ('asianne', 83), ('asiat', 80), ('italiann', 72), ('italiano', 72), ('italianne', 72), ('italian', 67), ('amurican', 62), ('american', 62), ('italiaan', 62), ('italiian', 62), ('itallian', 62), ('americann', 57), ('americano', 57), ('ameerican', 57), ('aamerican', 57), ('ameriican', 57), ('amerrican', 57), ('ammericann', 54), ('ameerrican', 54), ('ammereican', 54), ('america', 50), ('merican', 50), ('murican', 50), ('italien', 50), ('americen', 46), ('americin', 46), ('amerycan', 46), ('itali', 40)]
    [('american', 100), ('americann', 94), ('americano', 94), ('ameerican', 94), ('aamerican', 94), ('ameriican', 94), ('amerrican', 94), ('america', 93), ('merican', 93), ('ammericann', 89), ('ameerrican', 89), ('ammereican', 89), ('amurican', 88), ('americen', 88), ('americin', 88), ('amerycan', 88), ('murican', 80), ('asian', 62), ('asiane', 57), ('asiann', 57), ('asiian', 57), ('asiaan', 57), ('italian', 53), ('asianne', 53), ('italiann', 50), ('italiano', 50), ('italiaan', 50), ('italiian', 50), ('itallian', 50), ('italianne', 47), ('asiat', 46), ('itali', 40), ('italien', 40)]
    [('italian', 100), ('italiann', 93), ('italiano', 93), ('italiaan', 93), ('italiian', 93), ('itallian', 93), ('italianne', 88), ('italien', 86), ('itali', 83), ('asian', 67), ('asiane', 62), ('asiann', 62), ('asiian', 62), ('asiaan', 62), ('asianne', 57), ('amurican', 53), ('american', 53), ('americann', 50), ('asiat', 50), ('americano', 50), ('ameerican', 50), ('aamerican', 50), ('ameriican', 50), ('amerrican', 50), ('ammericann', 47), ('ameerrican', 47), ('ammereican', 47), ('america', 43), ('merican', 43), ('murican', 43), ('americen', 40), ('americin', 40), ('amerycan', 40)]
'''

'''
Instructions 2/2

Question

Take a look at the output, what do you think should be the similarity cutoff point
when remapping categories?

Possible Answers:

-> 80 [Correct]
-> 70 [X]
-> 60 [X]

80 is that sweet spot where you convert all incorrect typos without remapping incorrect 
categories. Often times though, you may need to combine the techniques learned in chapter 
2, especially since there could be strings that make it beyond our cutoff point, but are 
not actually a match!
'''
