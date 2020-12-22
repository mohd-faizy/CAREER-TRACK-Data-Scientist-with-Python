'''
10 - Subsetting pivot tables:

A pivot table is just a DataFrame with sorted indexes, so the techniques you 
have learned already can be used to subset them. In particular, the .loc[] + slicing 
combination is often helpful.

pandas is loaded as pd. temp_by_country_city_vs_year is available.

Instructions

Use .loc[] on temp_by_country_city_vs_year to take subsets.

- From Egypt to India.
- From Egypt, Cairo to India, Delhi.
- From Egypt, Cairo to India, Delhi, and 2005 to 2010.

----------------------------------------------------------------------------------------------------------
temp_by_country_city_vs_year.head()

year                     2000    2001    2002    2003    2004  ...    2009    2010    2011    2012    2013
country     city                                               ...                                        
Afghanistan Kabul      15.823  15.848  15.715  15.133  16.128  ...  15.093  15.676  15.812  14.510  16.206
Angola      Luanda     24.410  24.427  24.791  24.867  24.216  ...  24.325  24.440  24.151  24.240  24.554
Australia   Melbourne  14.320  14.180  14.076  13.986  13.742  ...  14.647  14.232  14.191  14.269  14.742
            Sydney     17.567  17.855  17.734  17.592  17.870  ...  18.176  17.999  17.713  17.474  18.090
Bangladesh  Dhaka      25.905  25.931  26.095  25.927  26.136  ...  26.536  26.648  25.803  26.284  26.587
----------------------------------------------------------------------------------------------------------
'''
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt", "Cairo"):("India", "Delhi"), "2005":"2010"]
