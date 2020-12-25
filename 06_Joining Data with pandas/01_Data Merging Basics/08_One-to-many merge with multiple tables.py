'''
08 - One-to-many merge with multiple tables

In  this  exercise,  assume  that  you are looking  to start a  business  in the city
of Chicago. Your perfect idea is to start a  company  that  uses  goats  to  mow  the
lawn for other businesses. However, you have to choose a location  in the city to put
your  goat  farm. You need a location  with  a great deal of space and relatively few 
businesses and people around to avoid complaints about the smell. You  will  need  to 
merge three tables to help you choose your location. The land_use table has  info  on 
the percentage of vacant land by city ward. The census table has  population by  ward,
 and the licenses table lists businesses by ward.

The land_use, census, and licenses tables have been loaded for you.

---------------------------------------------------------------------------------
land_use.head()

  ward  residential  commercial  industrial  vacant  other
0    1           41           9           2       2     46
1    2           31          11           6       2     50
2    3           20           5           3      13     59
3    4           22          13           0       7     58
4    5           25           3           1       3     68

census.head()

  ward  pop_2000  pop_2010 change                                  address    zip
0    1     52951     56149     6%              2765 WEST SAINT MARY STREET  60647
1    2     54361     55805     3%                 WM WASTE MANAGEMENT 1500  60622
2    3     40385     53039    31%                      17 EAST 38TH STREET  60653
3    4     51953     54589     5%  31ST ST HARBOR BUILDING LAKEFRONT TRAIL  60653
4    5     55302     51455    -7%  JACKSON PARK LAGOON SOUTH CORNELL DRIVE  60637

licenses.head()

  account ward  aid                   business               address    zip
0  307071    3  743       REGGIE'S BAR & GRILL       2105 S STATE ST  60616
1      10   10  829                 HONEYBEERS   13200 S HOUSTON AVE  60633
2   10002   14  775                CELINA DELI     5089 S ARCHER AVE  60632
3   10005   12  NaN  KRAFT FOODS NORTH AMERICA        2005 W 43RD ST  60609
4   10044   44  638  NEYBOUR'S TAVERN & GRILLE  3651 N SOUTHPORT AVE  60613

---------------------------------------------------------------------------------

Instructions:

- Merge land_use and census on the ward column. Merge the result of this with licenses on
  the ward column, using the suffix _cen for the left table and _lic for the right table. 
  Save this to the variable land_cen_lic.

- Group land_cen_lic by ward, pop_2010 (the population in 2010), and vacant, then count the
  number of accounts. Save the results to pop_vac_lic.

- Sort pop_vac_lic by vacant, account, andpop_2010 in descending, ascending, and ascending 
  order respectively. Save it as sorted_pop_vac_lic.

'''
# 1----------------------------------------------------------------------------------------
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \

# 2----------------------------------------------------------------------------------------
# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
    .merge(licenses, on='ward', suffixes=('_cen', '_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'],
                                   as_index=False).agg({'account': 'count'})

# 3----------------------------------------------------------------------------------------

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
    .merge(licenses, on='ward', suffixes=('_cen', '_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'],
                                   as_index=False).agg({'account': 'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'],
                                             ascending=[False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())
