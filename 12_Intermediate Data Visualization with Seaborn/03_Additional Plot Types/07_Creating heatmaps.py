'''
07 - Creating heatmaps

A heatmap is a common matrix plot that can be  used to graphically summarize
the relationship between two variables. For  this exercise, we will start by 
looking at guests of the Daily Show from 1999-2015 and see how the occupations
of the guests have changed over time.

The  data  includes the date of  each  guest  appearance  as well  as  their 
occupation. For the first exercise, we need to get the data into  the  right
format for Seaborn's heatmap function to correctly plot the data. All of the
data has already been read into the df variable.

Instructions

- Use pandas' crosstab() function to build a table of visits by Group and Year.
- Print the pd_crosstab DataFrame.
- Plot the data using Seaborn's heatmap().
'''
# Create a crosstab table of the data
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot a heatmap of the table
sns.heatmap(pd_crosstab)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

plt.show()
