'''
02 - Phillips curve using merge_ordered()

There is an economic theory developed by A. W. Phillips which states that inflation 
and unemployment have an inverse relationship. The theory claims that with  economic 
growth comes inflation, which in turn should lead to more jobs and less unemployment.

You will take two tables of data  from the U.S. Bureau  of  Labor  Statistics, containing 
unemployment and inflation data over  different periods,  and  create  a  Phillips  curve. 
The tables have different frequencies. One table has a data entry every six months, while 
the other has a data entry every month. You will need to use the entries where you have 
data within both tables.

The tables unemployment and inflation have been loaded for you.

---------------------------------------------------------------
unemployment.head()

         date  unemployment_rate
0  2013-06-01                7.5
1  2014-01-01                6.7
2  2014-06-01                6.1
3  2015-01-01                5.6
4  2015-06-01                5.3

inflation.head()

         date      cpi     seriesid                  data_type
0  2014-01-01  235.288  CUSR0000SA0  SEASONALLY ADJUSTED INDEX
1  2014-02-01  235.547  CUSR0000SA0  SEASONALLY ADJUSTED INDEX
2  2014-03-01  236.028  CUSR0000SA0  SEASONALLY ADJUSTED INDEX
3  2014-04-01  236.468  CUSR0000SA0  SEASONALLY ADJUSTED INDEX
4  2014-05-01  236.918  CUSR0000SA0  SEASONALLY ADJUSTED INDEX
---------------------------------------------------------------
Instructions

- Use merge_ordered() to merge the inflation and unemployment tables on date with an inner 
  join, and save the results as inflation_unemploy.Print the inflation_unemploy variable.

- Using inflation_unemploy, create a scatter plot with unemployment_rate on the horizontal 
  axis and cpi (inflation) on the vertical axis.
'''
# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment,
                                      on='date', how='inner')

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter', x='unemployment_rate', y='cpi')
plt.show()
