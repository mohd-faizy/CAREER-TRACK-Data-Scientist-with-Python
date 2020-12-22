'''
04 - Sorting by index values:
Previously, you changed the order of the rows in a DataFrame by calling .sort_values(). 
It's also useful to be able to sort by elements in the  index. For this,  you need  to  
use .sort_index().

pandas is loaded as pd. temperatures_ind has a multi-level index  of  country  and city,
and is available.

Instructions:

 - Sort temperatures_ind by the index values.
 
 - Sort temperatures_ind by the index values at the "city" level.
 
 - Sort temperatures_ind by ascending country then descending city.
 -------------------------------------------
 temperatures_ind

                            date  avg_temp_c
country       city                          
Côte D'Ivoire Abidjan 2000-01-01      27.293
              Abidjan 2000-02-01      27.685
              Abidjan 2000-03-01      29.061
              Abidjan 2000-04-01      28.162
              Abidjan 2000-05-01      27.547
---------------------------------------------
'''

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(
    level=["country", "city"], ascending=[True, False]))
