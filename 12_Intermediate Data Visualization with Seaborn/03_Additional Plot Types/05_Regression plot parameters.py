'''
05 - Regression plot parameters

Seaborn's regression plot supports several parameters that can be
used to configure the plots and drive more insight into the data.

For the next exercise, we can look  at the  relationship  between  tuition
and the percent of students that receive  Pell  grants. A  Pell  grant  is
based on student financial need and subsidized by the  US  Government.  In
this data set, each University has some percentage of students that receive
these grants. Since this data is continuous, using x_bins can be useful to
break the percentages into categories in order to summarize and understand
the data.
'''
# 1 - Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL")

plt.show()
plt.clf()

# 2 - Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()

# 3 - Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()
