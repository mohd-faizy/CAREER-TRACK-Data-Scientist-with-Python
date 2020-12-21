'''
06 - Counting categorical variables

Counting is a great  way  to  get  an  overview  of  your data
and to spot curiosities that you might not notice  otherwise.
In this exercise, you'll count the number of each type of store
and the number of each department number using the DataFrames
you created in the previous exercise:

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])

Instructions:

 - Count the number of stores of each store type in store_types.
 
 - Count the proportion of stores of each store type in store_types.
 
 - Count the number of different departments in store_depts, sorting the
   counts in descending order.
 
 - Count the proportion of different departments in store_depts, sorting 
   the proportions in descending order.

-----------------------------------------------------------------------------------------------------------------
store_types.head()

    store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
1      2    A           1 2010-02-05      35034.06       False          4.550                 0.679         8.324
2      4    A           1 2010-02-05      38724.42       False          6.533                 0.686         8.623
3      6    A           1 2010-02-05      25619.00       False          4.683                 0.679         7.259
4     10    B           1 2010-02-05      40212.84       False         12.411                 0.782         9.765
-----------------------------------------------------------------------------------------------------------------
store_depts.head()

   store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
1      1    A           2 2010-02-05      50605.27       False          5.728                 0.679         8.106
2      1    A           3 2010-02-05      13740.12       False          5.728                 0.679         8.106
3      1    A           4 2010-02-05      39954.04       False          5.728                 0.679         8.106
4      1    A           5 2010-02-05      32229.38       False          5.728                 0.679         8.106
-----------------------------------------------------------------------------------------------------------------
'''
# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)
