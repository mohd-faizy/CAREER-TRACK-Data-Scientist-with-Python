'''
07 - Validating a merge

You have been given 2 tables, artists, and albums. Use the console to merge them using
artists.merge(albums, on='artid').head(). Adjust the validate argument to answer which
statement is False.

Instructions

Possible Answers

-> You can use 'many_to_many' without an error, since there is a duplicate key in one of
   the tables.[X]

-> You can use 'one_to_many' without error, since there is a duplicate key in the right 
   table.[X]

-> You can use 'many_to_one' without an error, since there is a duplicate key in the left
    table.[✓]
'''
