'''
11 - Multiple plots

For the final exercise we will plot a comparison of the fair market rents for 1-bedroom and 2-bedroom apartments.

Instructions

- Create two axes objects, ax0 and ax1.
- Plot fmr_1 on ax0 and fmr_2 on ax1.
- Display the plots side by side.
'''
# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

# Plot the distribution of 1 bedroom apartments on ax0
sns.distplot(df['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500))

# Plot the distribution of 2 bedroom apartments on ax1
sns.distplot(df['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100, 1500))

# Display the plot
plt.show()
