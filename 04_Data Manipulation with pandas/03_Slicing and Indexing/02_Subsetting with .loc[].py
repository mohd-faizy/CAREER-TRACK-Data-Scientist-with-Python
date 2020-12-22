'''
02 - Subsetting with .loc[]

The killer feature for indexes is .loc[]: a subsetting method that accepts
index values. When you pass it a single argument, it will take a subset of
rows.

The code for subsetting using .loc[] can be easier to  read  than  standard
square bracket subsetting, which can make your code less burdensome to maintain.

Instructions:

 - Create a list called cities that contains "Moscow" and "Saint Petersburg".
 
 - Use [] subsetting to filter temperatures for rows where the city column takes a
   value in the cities list.
 
 - Use .loc[] subsetting to filter temperatures_ind for rows where the city is in
   the cities list.

 ------------------------------------------------
 temperatures.head()

         date     city        country  avg_temp_c
0 2000-01-01  Abidjan  Côte D'Ivoire      27.293
1 2000-02-01  Abidjan  Côte D'Ivoire      27.685
2 2000-03-01  Abidjan  Côte D'Ivoire      29.061
3 2000-04-01  Abidjan  Côte D'Ivoire      28.162
4 2000-05-01  Abidjan  Côte D'Ivoire      27.547
-------------------------------------------------
temperatures_ind.head()

              date        country  avg_temp_c
city                                         
Abidjan 2000-01-01  Côte D'Ivoire      27.293
Abidjan 2000-02-01  Côte D'Ivoire      27.685
Abidjan 2000-03-01  Côte D'Ivoire      29.061
Abidjan 2000-04-01  Côte D'Ivoire      28.162
Abidjan 2000-05-01  Côte D'Ivoire      27.547
-------------------------------------------------
'''
# Importing Pandas
import pandas as pd
temperatures = pd.read_csv('/contect/temperatures.csv')

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])