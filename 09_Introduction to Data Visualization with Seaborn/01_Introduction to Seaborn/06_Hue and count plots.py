'''
06 - Hue and count plots

Let's continue exploring our dataset from  students  in secondary school 
by looking at a new variable. The "school" column indicates the initials 
of which school the student attended - either "GP" or "MS".

In the last exercise, we created a scatter plot where the  plot  points  were 
colored based on whether the student lived in  an  urban or rural  area.  How 
many students live in urban vs. rural areas, and does this vary based on what 
school the student attends? Let's make a count plot with subgroups to find out.

Instructions

- Fill in the palette_colors dictionary to map the "Rural" location value to the
  color "green" and the "Urban" location value to the color "blue".

- Create a count plot with "school" on the x-axis using the student_data DataFrame.

  - Add subgroups to the plot using "location" variable and use the palette_colors 
    dictionary to make the location subgroups green and blue.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school",
                data=student_data,
                hue="location",
                palette=palette_colors)


# Display plot
plt.show()
