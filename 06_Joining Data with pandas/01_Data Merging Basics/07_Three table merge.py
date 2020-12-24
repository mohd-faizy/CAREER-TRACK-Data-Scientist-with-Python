'''
07 - Three table merge

To solidify the concept of a three DataFrame merge, practice another exercise. 
A reasonable extension of our review of Chicago business data would include
looking at demographics information about the neighborhoods where the businesses 
are. A table with the median income by zip code has been provided to you. You will
merge the licenses and wards tables with this new income-by-zip-code table called
zip_demo.

The licenses, wards, and zip_demo DataFrames have been loaded for you.

---------------------------------------------------------------------------
licenses.head()

  account ward  aid                   business               address    zip
0  307071    3  743       REGGIE'S BAR & GRILL       2105 S STATE ST  60616
1      10   10  829                 HONEYBEERS   13200 S HOUSTON AVE  60633
2   10002   14  775                CELINA DELI     5089 S ARCHER AVE  60632
3   10005   12  NaN  KRAFT FOODS NORTH AMERICA        2005 W 43RD ST  60609
4   10044   44  638  NEYBOUR'S TAVERN & GRILLE  3651 N SOUTHPORT AVE  60613

wards.head()

  ward            alderman                          address    zip
0    1  Proco "Joe" Moreno        2058 NORTH WESTERN AVENUE  60647
1    2       Brian Hopkins       1400 NORTH  ASHLAND AVENUE  60622
2    3          Pat Dowell          5046 SOUTH STATE STREET  60609
3    4    William D. Burns  435 EAST 35TH STREET, 1ST FLOOR  60616
4    5  Leslie A. Hairston            2325 EAST 71ST STREET  60649

zip_demo.head()

     zip  income
0  60630   70122
1  60640   50488
2  60622   87143
3  60614  100116
4  60608   41226
---------------------------------------------------------------------------

Instructions:

- Starting with the licenses table, merge to it the zip_demo table on the zip column. Then 
  merge the resulting table to the wards table on the ward column. Save result of the three 
  merged tables to a variable named licenses_zip_ward.

- Group the results of the three merged tables by the column alderman  and find  the median
  income.
  
'''
# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
    .merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income': 'median'}))
