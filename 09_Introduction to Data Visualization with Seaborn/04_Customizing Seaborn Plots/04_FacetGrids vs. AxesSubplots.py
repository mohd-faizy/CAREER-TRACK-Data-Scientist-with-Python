'''
04 - FacetGrids vs. AxesSubplots

In the recent lesson, we learned that Seaborn plot functions create 
two different types of objects: FacetGrid objects  and  AxesSubplot 
objects. The method for adding a title  to  your  plot  will  differ 
depending on the type of object it is.

In the code provided, we've used relplot() with the miles per gallon 
dataset to create a scatter plot showing the relationship between  a 
car's weight and its horsepower. This scatter plot is assigned to the 
variable name g. Let's identify which type of object it is.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions 1/2:

- Identify what type of object plot g is and assign it to the variable 
  type_of_g.
'''
# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)

'''
Instructions 2/2

Question:

We've just seen that sns.relplot() creates FacetGrid objects. Which other Seaborn
function creates a FacetGrid object instead of an AxesSubplot object?
~ Possible Answers ~

- sns.catplot()[Correct]
- sns.scatterplot()[X]
- sns.boxplot()[X]
- sns.countplot()[X]
'''
