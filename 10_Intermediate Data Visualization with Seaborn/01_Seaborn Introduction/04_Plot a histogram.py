'''
04 - Plot a histogram

The distplot() function will return a Kernel Density Estimate (KDE) by default. 
The KDE helps to smooth the distribution and is a useful way to look at the data.
However, Seaborn can also support the more standard histogram approach if that is
 more meaningful for your analysis.

Instructions:

- Create a distplot for the data and disable the KDE.
- Explicitly pass in the number 20 for the number of bins in the histogram.
- Display the plot using plt.show()
'''
# Create a distplot
sns.distplot(df['Award_Amount'],
             kde=False,
             bins=20)

# Display the plot
plt.show()
