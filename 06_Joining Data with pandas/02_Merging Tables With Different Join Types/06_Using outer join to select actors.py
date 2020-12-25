'''
06 - Using outer join to select actors

One cool aspect of using an outer join is that, because it returns all rows 
from both merged tables and null where they do not match, you can use it to 
iron_2_actors. Both tables have been loaded for you and a few rows  printed 
so you can see the structure.

Venn graph with no overlap
-----------------------------------------------------------------------------
>iron_1_actors.head()

                     character     id             name
3                       Yinsen  17857       Shaun Toub
4      Virginia "Pepper" Potts  12052  Gwyneth Paltrow
2  Obadiah Stane / Iron Monger   1229     Jeff Bridges
1                  War Machine  18288  Terrence Howard
7           Christine Everhart  57451      Leslie Bibb

>iron_2_actors.head()

                                          character     id                name
4                             Ivan Vanko / Whiplash   2295       Mickey Rourke
3  Natalie Rushman / Natasha Romanoff / Black Widow   1245  Scarlett Johansson
5                                     Justin Hammer   6807        Sam Rockwell
6                                Director Nick Fury   2231   Samuel L. Jackson
1                           Virginia "Pepper" Potts  12052     Gwyneth Paltrow
-----------------------------------------------------------------------------
Instructions:

- Save to iron_1_and_2 the merge of iron_1_actors (left) with iron_2_actors tables
  with an outer join on the id column, and set suffixes to ('_1','_2').

- Create an index that returns True if name_1 or name_2 are null, and False otherwise.
'''
# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                   on='id',
                                   how='outer',
                                   suffixes=('_1', '_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())
