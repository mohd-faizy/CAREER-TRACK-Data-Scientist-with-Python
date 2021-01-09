'''
03 - barplots, pointplots and countplots

The final group of categorical  plots  are  barplots,  pointplots  and
countplot which create statistical summaries of  the  data. The  plots 
follow a similar API as the other plots and allow further customization 
for the specific problem at hand
'''
# 1 - Countplots
# Create a countplot with the df dataframe and Model Selected on the y axis and the color varying by Region.
sns.countplot(data=df,
              y="Model Selected",
              hue="Region")

plt.show()
plt.clf()

# 2 - Pointplot
# - Create a pointplot with the df dataframe and Model Selected on the x-axis and Award_Amount on the y-axis.
# - Use a capsize in the pointplot in order to add caps to the error bars.
sns.pointplot(data=df,
              x='Model Selected',
              y='Award_Amount',
              capsize=.1)

plt.show()
plt.clf()


# 3 - barplot
# Create a barplot with the same data on the x and y axis and change the color of each bar based on the Region column.
sns.barplot(data=df,
            y='Award_Amount',
            x='Model Selected',
            hue='Region')

plt.show()
plt.clf()
