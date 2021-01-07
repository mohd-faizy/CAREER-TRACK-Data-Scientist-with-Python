'''
05 - Rug plot and kde shading

Now that you understand  some  function  arguments for  distplot(),  we 
can continue further refining  the output. This  process of creating  a 
visualization and updating it in an incremental fashion is a useful and 
common approach to look at data from multiple perspectives.

Seaborn excels at making this process simple.

Instructions:

- Create a distplot of the Award_Amount column in the df.
- Configure it to show a shaded kde (using the kde_kws dictionary).
- Add a rug plot above the x axis.
- Display the plot.
'''
# Create a distplot of the Award Amount
sns.distplot(df['Award_Amount'],
             hist=False,
             rug=True,
             kde_kws={'shade': True})

# Plot the results
plt.show()
