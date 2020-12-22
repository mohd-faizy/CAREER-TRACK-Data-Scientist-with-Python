'''
11 - Calculating on a pivot table:

Pivot tables are filled with summary statistics, but they are only a first 
step to finding something insightful. Often you'll need to perform further 
calculations on them. A common thing to do is to find the rows or columns where 
the highest or lowest value occurs.

Recall from Chapter 1 that you can easily subset a Series or DataFrame to find 
rows of interest using a logical condition inside of square brackets. 
For example: series[series > value].

pandas is loaded as pd and the DataFrame temp_by_country_city_vs_year is available.

Instructions:

 - Calculate the mean temperature for each year, assigning to mean_temp_by_year.
 - Filter mean_temp_by_year for the year that had the highest mean temperature.
 - Calculate the mean temperature for each city (across columns), assigning to mean_temp_by_city.
 - Filter mean_temp_by_city for the city that had the lowest mean temperature.

 --------------------------------------------------------------------------------------------------------
 temp_by_country_city_vs_year.head()

year                     2000    2001    2002    2003    2004  ...    2009    2010    2011    2012    2013
country     city                                               ...                                        
Afghanistan Kabul      15.823  15.848  15.715  15.133  16.128  ...  15.093  15.676  15.812  14.510  16.206
Angola      Luanda     24.410  24.427  24.791  24.867  24.216  ...  24.325  24.440  24.151  24.240  24.554
Australia   Melbourne  14.320  14.180  14.076  13.986  13.742  ...  14.647  14.232  14.191  14.269  14.742
            Sydney     17.567  17.855  17.734  17.592  17.870  ...  18.176  17.999  17.713  17.474  18.090
Bangladesh  Dhaka      25.905  25.931  26.095  25.927  26.136  ...  26.536  26.648  25.803  26.284  26.587
 --------------------------------------------------------------------------------------------------------
'''
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
