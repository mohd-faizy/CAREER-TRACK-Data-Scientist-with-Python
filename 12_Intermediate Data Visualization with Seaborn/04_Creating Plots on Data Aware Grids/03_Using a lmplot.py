'''
03 - Using a lmplot

The lmplot  is  used to  plot  scatter plots  with regression  lines 
on  FacetGrid  objects. The API  is  similar  to factorplot with the 
difference that the default behavior of lmplot is to plot regression 
lines.

For the first set of exercises, we  will  look  at  the  Undergraduate
population (UG) and compare it to the percentage of students receiving
Pell Grants (PCTPELL). 

For the second lmplot exercise, we can look at  the relationships  between 
Average SAT scores and Tuition across the different degree types and public
vs. non-profit schools.
'''
# 1/3---------------------------------------------------------------------------
# Create a FacetGrid with Degree_Type columns and scatter plot of UG and PCTPELL.
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)

# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL')

plt.show()
plt.clf()

# 2/3---------------------------------------------------------------------------
# Create a lmplot() using the same values from the FacetGrid().
# Re-create the plot above as an lmplot
sns.lmplot(data=df,
        x='UG',
        y='PCTPELL',
        col="Degree_Type",
        col_order=degree_ord)

plt.show()
plt.clf()

# 3/3---------------------------------------------------------------------------
# Create a facetted lmplot() comparing SAT_AVG_ALL to Tuition with columns varying by Ownership and rows by Degree_Type.
# In the lmplot() add a hue for Women Only Universities.
sns.lmplot(data=df,
           x='SAT_AVG_ALL',
           y='Tuition',
           col="Ownership",
           row='Degree_Type',
           row_order=['Graduate', 'Bachelors'],
           hue='WOMENONLY',
           col_order=inst_ord)

plt.show()
plt.clf()
