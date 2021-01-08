'''
05 - Using default palettes

Seaborn includes several default palettes that can be easily applied to your plots. 
In this example, we will look at the impact of two different palettes on  the  same 
distplot.

Instructions

- Create a for loop to show the difference between the bright and colorblind palette.
- Set the palette using the set_palette() function.
- Use a distplot of the fmr_3 column.

'''
# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()

    # Clear the plots
    plt.clf()
