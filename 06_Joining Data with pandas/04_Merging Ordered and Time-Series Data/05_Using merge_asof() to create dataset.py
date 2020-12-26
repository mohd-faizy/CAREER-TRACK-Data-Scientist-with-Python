'''
05 - Using merge_asof() to create dataset

The merge_asof() function can be used to create datasets  where you have  a  table  of  start 
and stop dates, and you want to use them to create a  flag in another  table. You  have  been 
given gdp, which is a table of quarterly GDP values of the US during the  1980s. Additionally, 
the table recession has been given to you. It holds the starting date  of every  US  recession 
since 1980, and the date when the recession was declared to be over. Use merge_asof() to merge 
the tables and create a status flag if a quarter was during a recession. Finally, to check your 
work, plot the data in a bar chart.

The tables gdp and recession have been loaded for you.
-------------------------
gdp.head()

        date       gdp
0 1979-01-01  2526.610
1 1979-04-01  2591.247
2 1979-07-01  2667.565
3 1979-10-01  2723.883
4 1980-01-01  2789.842

recession.head()

        date econ_status
0 1980-01-01   recession
1 1980-08-01      normal
2 1981-07-01   recession
3 1982-12-01      normal
4 1990-07-01   recession
-------------------------

Instructions

- Using merge_asof(), merge gdp and recession on date, with gdp as the left table. Save to the
  variable gdp_recession.

- Create a list using a list comprehension and a conditional expression, named is_recession, where
  for each row if the gdp_recession['econ_status'] value is equal to 'recession' then enter 'r' else 'g'.

- Using gdp_recession, plot a bar chart of gdp versus date, setting the color argument equal to is_recession.
'''
# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on='date')

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s =='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', x='date', color=is_recession, rot=90)
plt.show()
