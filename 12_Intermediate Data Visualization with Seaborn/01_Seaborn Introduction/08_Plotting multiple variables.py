'''
08 - Plotting multiple 

Since we are using lmplot() now, we can look at  the  more  complex 
interactions of data. This data set includes geographic information 
by state and area. It might be interesting  to  see  if  there  is  
a  difference in relationships based on the Region of the country.

Instructions:

- Use lmplot() to look at the relationship between insurance_losses and
  premiums.
- Plot a regression line for each Region of the country.
'''
# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()
