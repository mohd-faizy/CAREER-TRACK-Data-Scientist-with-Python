'''
04 - Using merge_asof() to study stocks

Using merge_asof() to study stocks
You have a feed of stock  market  prices that  you  record. You  attempt  to 
track the price  every five minutes.  Still, due  to  some  network  latency, 
the prices you  record are  roughly  every 5  minutes. You  pull  your  price 
logs  for three  banks, JP  Morgan  (JPM), Wells  Fargo  (WFC), and  Bank  Of 
America (BAC). You want to know how the price change of the two  other  banks
compare to JP Morgan. Therefore, you will need to merge these three logs into 
one table. Afterward, you will use the pandas .diff() method to  compute  the 
price change over time. Finally, plot the price changes so you can review your 
analysis.

The three log files have been loaded for you as tables named jpm, wells, and bac.
-----------------------------
jpm.head()

            date_time    close
0 2017-11-17 15:35:17  98.1200
1 2017-11-17 15:40:04  98.1800
2 2017-11-17 15:45:01  97.7307
3 2017-11-17 15:50:55  97.7400
4 2017-11-17 15:55:00  97.8150

wells.head()

            date_time    close
0 2017-11-17 15:35:08  54.3227
1 2017-11-17 15:40:00  54.3200
2 2017-11-17 15:45:32  54.1900
3 2017-11-17 15:50:07  54.1700
4 2017-11-17 15:55:00  54.1841

bac.head()

            date_time   close
0 2017-11-17 15:35:17  26.552
1 2017-11-17 15:40:06  26.552
2 2017-11-17 15:45:05  26.388
3 2017-11-17 15:50:34  26.378
4 2017-11-17 15:55:06  26.383
-----------------------------
Instructions

- Use merge_asof() to merge jpm (left table) and wells together on the date_time 
  column, where the rows with the nearest times are matched, and with suffixes=('', '_wells').
  Save to jpm_wells.

- Use merge_asof() to merge jpm_wells (left table) and bac together on the date_time column,
  where the rows with the closest times are matched, and with suffixes=('_jpm', '_bac'). Save
  to jpm_wells_bac.
  
- Using price_diffs, create a line plot of the close price of JPM, WFC, and BAC only.
'''
# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time',
                              suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()
