'''
06 - Adding a title and axis labels

Let's continue  to look  at the  miles per  gallon  dataset. 
This time we'll create a line plot to  answer the  question: 
How does the average miles per gallon achieved by cars change
over time for each of the three places of origin? To  improve 
the readability of this  plot, we'll  add a  title  and  more 
informative axis labels.

In the code provided, we create the line plot using the lineplot()
function. Note that lineplot() does not support the creation of subplots,
so it returns an AxesSubplot object instead of an FacetGrid object.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions 1/2:

- Add the following title to the plot: "Average MPG Over Time".
'''
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean",
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title('Average MPG Over Time')

# Show plot
plt.show()

'''
Instructions 2/2

- Label the x-axis as "Car Model Year" and the y-axis as "Average MPG".
'''
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean",
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year",
      ylabel="Average MPG")

# Show plot
plt.show()
