'''
06 - Slicing in both directions

You've seen slicing DataFrames by rows and by columns, but since DataFrames
are two-dimensional objects, it is often natural to slice both dimensions at
once. That is, by passing two arguments to .loc[], you can subset by rows and
columns in one go.

pandas is loaded as pd. temperatures_srt is indexed by country and city, has a
sorted index, and is available.

Instructions:

 - Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
 
 - Use .loc[] slicing to subset columns from date to avg_temp_c.
 
 - Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.

----------------------------------------
temperatures_srt.head()
                        date  avg_temp_c
country     city                        
Afghanistan Kabul 2000-01-01       3.326
            Kabul 2000-02-01       3.454
            Kabul 2000-03-01       9.612
            Kabul 2000-04-01      17.925
            Kabul 2000-05-01      24.658
----------------------------------------
'''
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])
