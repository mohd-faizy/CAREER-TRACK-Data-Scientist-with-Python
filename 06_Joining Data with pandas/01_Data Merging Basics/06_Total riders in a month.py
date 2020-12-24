'''
06 - Total riders in a month:

Your  goal  is to find the total  number  of  rides  provided to  passengers  passing
through the Wilson station (station_name == 'Wilson') when  riding  Chicago's  public 
transportation  system  on  weekdays  (day_type == 'Weekday')  in  July  (month == 7). 
Luckily, Chicago provides this detailed data, but  it is  in three  different  tables. 
You will work on merging these tables  together to  answer the question. This data is 
different from the business related data you have seen so far, but all the information 
you need to answer the question is below.

The cal, ridership, and stations DataFrames have been loaded for you. The relationship 
between the tables can be seen in the diagram below.
--------          --------------         ------------
  cal                ridership             stations
--------          --------------         ------------
- year---------+    - station_id-------> - station_id
- month-----+  |--> - year               - station_name
- day-----+ |-----> - month              - location
- day_type|-------> - day
                    - rides

Table diagram. The cal table relates to ridership via year, month, and day. The ridership 
table relates to the stations table via station_id.

-----------------------------------------------------------------------------------------
cal.head()

   year  month  day        day_type
0  2019      1    1  Sunday/Holiday
1  2019      1    2         Weekday
2  2019      1    3         Weekday
3  2019      1    4         Weekday
4  2019      1    5        Saturday

ridership.head()

  station_id  year  month  day  rides
0      40010  2019      1    1    576
1      40010  2019      1    2   1457
2      40010  2019      1    3   1543
3      40010  2019      1    4   1621

stations.head()

  station_id        station_name                 location
0      40010  Austin-Forest Park  (41.870851, -87.776812)
1      40020         Harlem-Lake  (41.886848, -87.803176)
2      40030        Pulaski-Lake  (41.885412, -87.725404)
3      40040        Quincy/Wells   (41.878723, -87.63374)
4      40050               Davis   (42.04771, -87.683543)
-------------------------------------------------------------------------------------------
Instructions:

- Merge the ridership and cal tables together, starting with the ridership table on the left 
  and save the result to the variable ridership_cal. If you code takes too long to run, your 
  merge conditions might be incorrect.

- Extend the previous merge to three tables by also merging the stations table.

'''
# 1----------------------------------------------------------------------------------------
# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])

# 2----------------------------------------------------------------------------------------
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
    .merge(stations, on='station_id')

# 3----------------------------------------------------------------------------------------
# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)

