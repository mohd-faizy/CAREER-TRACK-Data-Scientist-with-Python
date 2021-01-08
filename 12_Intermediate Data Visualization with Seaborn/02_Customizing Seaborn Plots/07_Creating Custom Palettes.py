'''
07 - Creating Custom Palettes

Choosing a cohesive palette that works for your data can be time consuming.
Fortunately, Seaborn provides the color_palette() function to create your own
custom sequential, categorical, or diverging palettes. Seaborn also makes it
easy to view your palettes by using the palplot() function.

In this exercise, you can experiment with creating different palettes.
'''

for p in sns.palettes.SEABORN_PALETTES:
sns.set_palette(p)
sns.palplot(sns.color_palette())
plt.show()


# 1 - Create and display a Purples sequential palette containing 8 colors.ette
sns.palplot(sns.color_palette("Purples", 8))
plt.show()

# 2 - Create and display a palette with 10 colors using the husl system.
# Create the Purples palette
sns.palplot(sns.color_palette("husl", 10))
plt.show()

# 3 - Create and display a diverging palette with 6 colors coolwarm
# Create the Purples palette
sns.palplot(sns.color_palette("husl", 10))
plt.show()
