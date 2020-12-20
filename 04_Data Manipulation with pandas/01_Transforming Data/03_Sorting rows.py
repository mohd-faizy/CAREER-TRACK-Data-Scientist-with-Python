'''
03 - Sorting rows

Finding interesting bits of data in a DataFrame is often easier if you change the
order of the rows. You can sort the rows by passing a column name to .sort_values().

In cases where rows have the same value (this is common if you sort on a categorical
variable), you may wish to break the ties by sorting on another column. You can sort
on multiple columns in this way by passing a list of column names.

|Sort on …            |	Syntax                                   |
|---------------------|------------------------------------------|
|- one column         | - df.sort_values("breed")                |
|- multiple columns   | - df.sort_values(["breed", "weight_kg"]) |
|---------------------|------------------------------------------|

By combining .sort_values() with .head(), you can answer questions in the form,
"What are the top cases where…?".

Instructions 1/3:

 1. Sort homelessness by the number of homeless individuals, from smallest to largest,
    and save this as homelessness_ind.

    - Print the head of the sorted DataFrame.
 
 2. Sort homelessness by the number of homeless family_members in descending order, and
    save this as homelessness_fam.

    - Print the head of the sorted DataFrame.

 3. Sort homelessness first by region (ascending), and then by number of family members
   (descending). Save this as homelessness_reg_fam.

    - Print the head of the sorted DataFrame.
--------------------------------------------------------------------------
homelessness.head()

               region       state  individuals  family_members  state_pop
0  East South Central     Alabama       2570.0           864.0    4887681
1             Pacific      Alaska       1434.0           582.0     735139
2            Mountain     Arizona       7259.0          2606.0    7158024
3  West South Central    Arkansas       2280.0           432.0    3009733
4             Pacific  California     109008.0         20964.0   39461588
---------------------------------------------------------------------------
'''
# Import pandas using the alias pd
import pandas as pd
homelessness = pd.read_csv('content/homelessness.csv')

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(
    ['region', 'family_members'], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())
