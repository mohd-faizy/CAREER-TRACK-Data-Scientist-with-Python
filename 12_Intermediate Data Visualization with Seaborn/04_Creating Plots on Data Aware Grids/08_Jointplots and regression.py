'''
08 - Jointplots and regression

Since the previous plot does not show a relationship between humidity 
and rental amounts, we can look at another variable  that  we  reviewed 
earlier. Specifically, the relationship between temp and total_rentals.

Instructions 1/2

- Create a jointplot with a 2nd order polynomial regression plot comparing temp
  and total_rentals.
'''
# Plot a jointplot showing the residuals
sns.___(x="temp",
        y="total_rentals",
        kind='____',
        data=df,
        order=2)

plt.show()
plt.clf()


'''
Instructions 2/2

- Use a residual plot to check the appropriateness of the model.
'''
sns.jointplot(x="temp",
              y="total_rentals",
              kind='resid',
              data=df,
              order=2)

plt.show()
plt.clf()
