'''
01 - Setting and removing indexes

pandas allows you to designate columns as an index. This enables cleaner code
when  taking  subsets (as well as providing more  efficient lookup under some
circumstances).

Dataset: temperatures - a DataFrame of average temperatures in cities around
the world. 

Instructions

 - Look at temperatures.
 
 - Set the index of temperatures to "city", assigning to temperatures_ind.

 - Look at temperatures_ind. How is it different from temperatures?
 
 - Reset the index of temperatures_ind, keeping its contents.
 
 - Reset the index of temperatures_ind, dropping its contents.
 ------------------------------------------------
 temperatures.head()

         date     city        country  avg_temp_c
0 2000-01-01  Abidjan  Côte D'Ivoire      27.293
1 2000-02-01  Abidjan  Côte D'Ivoire      27.685
2 2000-03-01  Abidjan  Côte D'Ivoire      29.061
3 2000-04-01  Abidjan  Côte D'Ivoire      28.162
4 2000-05-01  Abidjan  Côte D'Ivoire      27.547
-------------------------------------------------
'''
# Importing Pandas 
import pandas as pd
temperatures = pd.read_csv('/contect/temperatures.csv')

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))


