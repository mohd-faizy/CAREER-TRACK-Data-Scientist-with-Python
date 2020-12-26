'''
05 - Concatenating with keys

The leadership of the music streaming company has come to you  and  asked  you 
for assistance in analyzing sales for a recent  business  quarter. They  would 
like to know which month in the quarter saw the highest average invoice total.
You have been given three tables with invoice data named inv_jul, inv_aug, and
inv_sep. Concatenate these tables into one to create a graph of the average 
monthly invoice total.

inv_jul.head()

   iid  cid invoice_date  total       bill_ctry
0   42   51   2009-07-06   1.98          Sweden
1   43   53   2009-07-06   1.98              UK
2   44   55   2009-07-07   3.96       Australia
3   45   59   2009-07-08   5.94           India
4   46    6   2009-07-11   8.91  Czech Republic

inv_aug.head()

   iid  cid invoice_date  total bill_ctry
0   49   30   2009-08-06   1.98    Canada
1   50   32   2009-08-06   1.98    Canada
2   51   34   2009-08-07   3.96  Portugal
3   52   38   2009-08-08   5.94   Germany
4   53   44   2009-08-11   8.91   Finland

inv_sep.head()

   iid  cid invoice_date  total bill_ctry
0   56    9   2009-09-06   1.98   Denmark
1   57   11   2009-09-06   1.98    Brazil
2   58   13   2009-09-07   3.96    Brazil
3   59   17   2009-09-08   5.94       USA
4   60   23   2009-09-11   8.91       USA

Instructions:

- Concatenate the three tables together vertically in order with the oldest month first,
  adding '7Jul', '8Aug', and '9Sep' as keys for their  respective  months, and  save  to 
  variable avg_inv_by_month.

- Use the .agg() method to find the average of the total column from the grouped invoices.

- Create a bar chart of avg_inv_by_month.
'''
# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                            ignore_index=False,
                            keys=['7Jul', '8Aug', '9Sep'])

print(inv_jul_thr_sep.head(50))

'''
In this problem, the .agg() method expects a dictionary with the column name as the key, 
and a function for the dictionary value.
'''
# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total': 'mean'})

print(avg_inv_by_month.head())

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind='bar')
plt.show()
