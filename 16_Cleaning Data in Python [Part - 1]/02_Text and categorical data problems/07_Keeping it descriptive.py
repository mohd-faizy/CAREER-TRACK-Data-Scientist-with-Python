'''
07 - Keeping it descriptive

To further understand travelers' experiences in the San  Francisco  Airport, 
the quality assurance department sent out a qualitative questionnaire to all 
travelers who gave the airport the worst score  on  all possible  categories. 
The objective behind this questionnaire is to identify common  patterns  in 
what travelers are saying about the airport.

Their response is stored in the survey_response column. Upon a  closer  look, 
you realized a few of the answers gave the shortest possible character amount 
without much substance. In this exercise, you will isolate the responses with 
a character count higher than 40 , and make sure your new DataFrame  contains 
responses with 40 characters or more using an assert statement.

The airlines DataFrame is in your environment, and pandas is imported as pd.

Instructions

- Using the airlines DataFrame, store the length of each instance in the 
  survey_response column in resp_length by using .str.len().

- Isolate the rows of airlines with resp_length higher than 40.

- Assert that the smallest survey response length in airlines_survey is now
  bigger than 40.
'''
# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])


'''
<script.py> output:
    18    The airport personnell forgot to alert us of d...
    19    The food in the airport was really really expe...
    20    One of the other travelers was really loud and...
    21    I don't remember answering the survey with the...
    22    The airport personnel kept ignoring my request...
    23    The chair I sat in was extremely uncomfortable...
    24    I wish you were more like other airports, the ...
    25    I was really unsatisfied with the wait times b...
    27    The flight was okay, but I didn't really like ...
    28    We were really slowed down by security measure...
    29    There was a spill on the aisle next to the bat...
    30    I felt very unsatisfied by how long the flight...
    Name: survey_response, dtype: object
'''
