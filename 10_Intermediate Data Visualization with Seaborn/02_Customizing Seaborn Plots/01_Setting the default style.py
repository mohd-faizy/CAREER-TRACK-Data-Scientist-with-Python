'''
01_Setting the default style

For these exercises, we will be looking at fair market rent values  calculated  by  the
US Housing and Urban Development Department. This data is used to  calculate  guidelines 
for several federal programs. The actual values for rents vary  greatly  across  the US.
We can use this data to get some experience with configuring Seaborn plots.

All of the necessary imports for seaborn, pandas and matplotlib have been completed. The
data is stored in the pandas DataFrame df.

By the way, if you haven't downloaded it already, check out the Seaborn Cheat  Sheet.  It 
includes an overview of the most important concepts, functions and methods and might come 
in handy if you ever need a quick refresher!

Instructions:

- Plot a pandas histogram without adjusting the style.
- Set Seaborn's default style.
- Create another pandas histogram of the fmr_2 column which represents fair market rent for
  a 2-bedroom apartment.
'''
# Plot the pandas histogram
df['fmr_2'].plot.hist()
plt.show()
plt.clf()

# Set the default seaborn style
sns.set()

# Plot the pandas histogram again
df['fmr_2'].plot.hist()
plt.show()
plt.clf()