'''
04 - How many rows with a left join?

Select the true statement about left joins.

Try running the following code statements in the console.

left_table.merge(one_to_one, on='id', how='left').shape
left_table.merge(one_to_many, on='id', how='left').shape
Note that the left_table starts out with 4 rows.

Instructions:

Possible Answers

- The output of a one-to-one merge with a left join will have more rows than the left table.[X]

- The output of a one-to-one merge with a left join will have fewer rows than the left table.[X]

- The output of a one-to-many merge with a left join will have greater than or equal rows than the left table.[✓]


In [2]:
left_table.merge(one_to_one, on='id', how='left').shape

Out[2]:
(4, 5)

In [3]:
left_table.merge(one_to_many, on='id', how='left').shape

Out[3]:
(232, 6)
'''
