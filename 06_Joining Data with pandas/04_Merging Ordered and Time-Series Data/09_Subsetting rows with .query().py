'''
09 - Subsetting rows with .query()

In this exercise, you will revisit GDP and population data  for  Australia  and 
Sweden from the World Bank and expand on it using the .query()  method.  You'll 
merge the two tables and compute the GDP per capita. Afterwards, you'll use the 
.query() method to sub-select the rows and create a plot. Recall that you  will 
need to merge on multiple columns in the proper order.

The tables gdp and pop have been loaded for you.
---------------------------------------------------
gdp.head()

        date    country          gdp    series_code
0 1990-01-01  Australia  158051.1324  NYGDPMKTPSAKD
1 1990-04-01  Australia  158263.5816  NYGDPMKTPSAKD
2 1990-07-01  Australia  157329.2790  NYGDPMKTPSAKD
3 1990-09-01  Australia  158240.6781  NYGDPMKTPSAKD
4 1991-01-01  Australia  156195.9535  NYGDPMKTPSAKD

pop.head()

        date    country       pop  series_code
0 1990-01-01  Australia  17065100  SP.POP.TOTL
1 1991-01-01  Australia  17284000  SP.POP.TOTL
2 1992-01-01  Australia  17495000  SP.POP.TOTL
3 1993-01-01  Australia  17667000  SP.POP.TOTL
4 1990-01-01     Sweden   8558835  SP.POP.TOTL
---------------------------------------------------

Instructions 1/4

- Use merge_ordered() on gdp and pop on columns country and date with the fill feature,
  save to gdp_pop and print.
'''
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

'''
Instructions 2/4
- Add a column named gdp_per_capita to gdp_pop that divides gdp by pop
'''
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']


'''
Instructions 3/4
- Pivot gdp_pop so values='gdp_per_capita', index='date', and columns='country', save as gdp_pivot.
'''
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(
    gdp, pop, on=['country', 'date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot table of gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

'''
Instructions 4/4
- Use .query() to select rows from gdp_pivot where date is greater than equal to 1991-01-01". Save as 
  recent_gdp_pop.
'''
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country', 'date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()
