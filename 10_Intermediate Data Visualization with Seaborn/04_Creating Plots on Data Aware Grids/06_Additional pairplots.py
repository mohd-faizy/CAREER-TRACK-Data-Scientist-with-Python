'''
06 - Additional pairplots

This exercise will go through a couple of more examples of how the pairplot()
can be customized for quickly analyzing data and determining areas of interest
that might be worthy of additional analysis.

One area of customization that is useful is to explicitly define the x_vars and
y_vars that you wish to examine. Instead of examining all pairwise relationships,
this capability allows you to look only at the specific interactions that may be
of interest.

We have already looked at using kind to control the types of plots. We can also
use diag_kind to control the types of plots shown on the diagonals. In the final
example, we will include a regression and kde plot in the pairplot.

Instructions 1/2

- Create a pair plot that examines fatal_collisions_speeding and fatal_collisions_alc
  on the x axis and premiums and insurance_losses on the y axis.
- Use the husl palette and color code the scatter plot by Region.
'''
# Build a pairplot with different x and y variables
sns.pairplot(data=df,
             x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"],
             y_vars=['premiums', 'insurance_losses'],
             kind='scatter',
             hue='Region',
             palette='husl')

plt.show()
plt.clf()

'''
Instructions 2/2

- Build a pairplot() with kde plots along the diagonals. Include the insurance_losses
  and premiums as the variables.
- Use a reg plot for the the non-diagonal plots.
- Use the BrBG palette for the final plot.
'''
sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg',
             palette='BrBG',
             diag_kind='kde',
             hue='Region')

plt.show()
plt.clf()
