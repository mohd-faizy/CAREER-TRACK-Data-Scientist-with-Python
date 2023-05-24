'''
07 - Create a regression plot

For this set of exercises, we will be looking at FiveThirtyEight's data on which US
State has the worst drivers. The data set includes summary level  information  about 
fatal accidents as well as insurance premiums for each state as of 2010.

In this exercise, we will look at the difference between the regression plotting functions.

Instructions 1/2

- The data is available in the dataframe called df.
- Create a regression plot using regplot() with "insurance_losses" on the x axis and "premiums" 
  on the y axis.
'''
# Create a regression plot of premiums vs. insurance_losses
sns.regplot(x="insurance_losses",
            y="premiums",
            data=df)

# Display the plot
plt.show()

'''
Instructions 2/2

- Create a regression plot of "premiums" versus "insurance_losses" using lmplot().
- Display the plot.
'''
# Create an lmplot of premiums vs. insurance_losses
sns.lmplot(x="insurance_losses",
           y="premiums",
           data=df)

# Display the second plot
plt.show()
