'''
03 - Inner joins and number of rows returned

All of the merges you have studied to this point are called inner joins.
 It is necessary to understand that inner joins only return the rows with 
 matching values in both tables. You will explore this further by reviewing
  the merge shown in the video lesson between the wards and census tables. 
  You will alter the tables and examine how this affects the merge between 
  them. The wards and census tables have been loaded for you.

For this exercise, it is important to know that both tables start with 50 rows,
 and are reset back to their original values after each Step.

Instructions:

- Merge wards and census on the ward column and save the result to wards_census.

- In the wards table, within the ward column, change the value of '1' to '61'.

- In the census table (not ward), within the ward column, change the value of '1' to None.
  - Print the shape of the wards_census.
----------------------------------------------------------------------------------
wards.head()

  ward            alderman                          address    zip
0    1  Proco "Joe" Moreno        2058 NORTH WESTERN AVENUE  60647
1    2       Brian Hopkins       1400 NORTH  ASHLAND AVENUE  60622
2    3          Pat Dowell          5046 SOUTH STATE STREET  60609
3    4    William D. Burns  435 EAST 35TH STREET, 1ST FLOOR  60616
4    5  Leslie A. Hairston            2325 EAST 71ST STREET  60649
census.head()

  ward  pop_2000  pop_2010 change                                  address    zip
0    1     52951     56149     6%              2765 WEST SAINT MARY STREET  60647
1    2     54361     55805     3%                 WM WASTE MANAGEMENT 1500  60622
2    3     40385     53039    31%                      17 EAST 38TH STREET  60653
3    4     51953     54589     5%  31ST ST HARBOR BUILDING LAKEFRONT TRAIL  60653
4    5     55302     51455    -7%  JACKSON PARK LAGOON SOUTH CORNELL DRIVE  60637
----------------------------------------------------------------------------------
'''
# 1---------------------------------------------------
# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print(wards_census.shape)

# 2---------------------------------------------------
# In the ward column change '1' to '61'
wards.loc[wards['ward'] == '1', 'ward'] = '61'

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print(wards_census.shape)

# 3---------------------------------------------------
# Change '1' to None in `ward` col of census
census.loc[census['ward'] == '1', 'ward'] = None

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print(wards_census.shape)
