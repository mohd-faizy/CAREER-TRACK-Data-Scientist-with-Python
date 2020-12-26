'''
12 - Using .melt() for stocks vs bond performance

It is widespread knowledge that the price of bonds is inversely related to  the  price 
of stocks. In this last exercise, you'll review many of the topics in this chapter  to 
confirm this. You have been given a table of percent change of the US 10-year treasury 
bond price. It is in a wide format where there is a separate column for each year. You 
will need to use the .melt() method to reshape this table.

Additionally, you will use the .query() method to filter out unneeded data. You will
merge this table with a table of the percent change of the Dow Jones Industrial stock 
index price. Finally, you will plot data.

The tables ten_yr and dji have been loaded for you.
-------------------------------------------------------------------------------------------------------------------------
ten_yr.head()

  metric  2007-02-01  2007-03-01  2007-04-01  2007-05-01  ...  2009-08-01  2009-09-01  2009-10-01  2009-11-01  2009-12-01
0   open    0.033491   -0.060449    0.025426   -0.004312  ...   -0.006687   -0.046564   -0.032068    0.034347   -0.050544
1   high   -0.007338   -0.040657    0.022046    0.030576  ...    0.031864   -0.090324    0.012447   -0.004191    0.099327
2    low   -0.016147   -0.007984    0.031075   -0.002168  ...    0.039510   -0.035946   -0.050733    0.030264    0.007188
3  close   -0.057190    0.021538   -0.003873    0.056156  ...   -0.028563   -0.027639    0.025703   -0.056309    0.200562

[4 rows x 36 columns]

dji.head()

         date     close
0  2007-02-01  0.005094
1  2007-03-01 -0.026139
2  2007-04-01  0.048525
3  2007-05-01  0.052007
4  2007-06-01 -0.016070
-------------------------------------------------------------------------------------------------------------------------

Instructions

- Use .melt() on ten_yr to unpivot everything except the metric column, setting var_name='date'
  and value_name='close'. Save the result to bond_perc.

- Using the .query() method, select only those rows were metric equals 'close', and save to 
  bond_perc_close.

- Use merge_ordered() to merge dji (left table) and bond_perc_close on date with an inner join, 
  and set suffixes equal to ('_dow', '_bond'). Save the result to dow_bond.

- Using dow_bond, plot only the Dow and bond values.

'''
# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on='date',
                            suffixes=('_dow', '_bond'), how='inner')

# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()
