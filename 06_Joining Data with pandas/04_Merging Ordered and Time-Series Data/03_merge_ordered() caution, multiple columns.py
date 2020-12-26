'''
03 - merge_ordered() caution, multiple columns

When using merge_ordered() to merge on  multiple  columns, the  order  is  important
when you combine it with the forward fill  feature. The  function  sorts  the  merge
on columns in the order provided. In this exercise, we will merge GDP and population
data from the World Bank for the Australia and Sweden, reversing the  order  of  the 
merge on columns. The frequency of the series  are  different, the  GDP  values  are 
quarterly, and the population is yearly. Use the forward fill feature to fill in the 
missing data. Depending on the order provided, the fill forward will use unintended 
data to fill in the missing values.

The tables gdp and pop have been loaded.

Instructions 1/2

- Use merge_ordered() on gdp and pop, merging on columns date and country with
  the fill feature, save to ctry_date.
'''
# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'],
                             fill_method='ffill')

# Print ctry_date
print(ctry_date)

'''
Instructions 2/2

- Perform the same merge of gdp and pop, but join on country and date (reverse of step 1) 
  with the fill feature, saving this as date_ctry.
'''
# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country', 'date'],
                             fill_method='ffill')

# Print date_ctry
print(date_ctry)
