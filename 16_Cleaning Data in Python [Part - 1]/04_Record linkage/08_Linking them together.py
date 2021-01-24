'''
08 - Linking them together!

In the last lesson, you've finished the bulk  of  the work  on  your 
effort to  link  restaurants and  restaurants_new. You've  generated 
the different pairs of potentially matching rows, searched for exact
 matches between the cuisine_type and city columns, but compared for 
 similar strings in the rest_name column. You stored the DataFrame 
 containing the scores in potential_matches.

Now it's finally time to link  both  DataFrames. You  will  do  so  by 
first extracting all row indices of restaurants_new that are  matching 
across the columns mentioned  above  from  potential_matches. Then you 
will subset restaurants_new on these indices, then append the non-duplicate 
values to restaurants. All DataFrames are in your environment, alongside 
pandas imported as pd.

Instructions:

- Isolate instances of potential_matches where the row sum is above or equal
  to 3 by using the .sum() method.

- Extract the second column index from matches, which represents row indices 
  of matching record from restaurants_new by using the .get_level_values() method.

- Subset restaurants_new for rows that are not in matching_indices.

- Append non_dup to restaurants.
'''
# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)

'''
<script.py> output:
                        rest_name                  rest_addr               city  \
    0   arnie morton's of chicago   435 s. la cienega blv .         los angeles   
    1          art's delicatessen       12224 ventura blvd.         studio city   
    2                   campanile       624 s. la brea ave.         los angeles   
    3                       fenix    8358 sunset blvd. west           hollywood   
    4          grill on the alley           9560 dayton way         los angeles   
    ..                        ...                        ...                ...   
    76                        don        1136 westwood blvd.           westwood   
    77                      feast        1949 westwood blvd.            west la   
    78                   mulberry        17040 ventura blvd.             encino   
    80                    jiraffe      502 santa monica blvd       santa monica   
    81                   martha's  22nd street grill 25 22nd  st. hermosa beach   
    
             phone cuisine_type  
    0   3102461501     american  
    1   8187621221     american  
    2   2139381447     american  
    3   2138486677     american  
    4   3102760615     american  
    ..         ...          ...  
    76  3102091422      italian  
    77  3104750400      chinese  
    78  8189068881        pizza  
    80  3109176671  californian  
    81  3103767786     american  
    
'''
