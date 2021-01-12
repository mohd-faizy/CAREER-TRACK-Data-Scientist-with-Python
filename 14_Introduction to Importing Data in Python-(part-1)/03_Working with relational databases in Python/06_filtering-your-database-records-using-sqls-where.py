'''
06 - Filtering your database records using SQL's WHERE


You can now execute a basic SQL query to select records from any table in your
database and you can also perform simple query customizations to select particular
columns and numbers of rows.

There are a couple more standard SQL query chops that will aid you in your journey
to becoming an SQL ninja.

Let's say, for example that you wanted to get all records from the Customer table of
the Chinook database for which the Country is 'Canada'. You can do this very easily
in SQL using a SELECT statement followed by a WHERE clause as follows:
-----------------------------------------------
SELECT * FROM Customer WHERE Country = 'Canada'
-----------------------------------------------

In fact, you can filter any SELECT statement by any condition using a WHERE clause.
This is called filtering your records.

In this interactive exercise, you'll select all records of the Employee table for which
'EmployeeId' is greater than or equal to 6.

Packages are already imported as follows:
-----------------------------------------
import pandas as pd
from sqlalchemy import create_engine
-----------------------------------------

Query away!

Instructions:

- Complete the argument of create_engine() so that the engine for the SQLite database
  'Chinook.sqlite' is created.

- Execute the query that selects all records from the Employee table where 'EmployeeId'
  is greater than or equal to 6. Use the >= operator and assign the results to rs.

- Apply the method fetchall() to rs in order to fetch all records in rs. Store them in
  the DataFrame df.

- Using the rs object, set the DataFrame's column names to the corresponding names of
  the table columns.
'''
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeID >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())

'''
Output
<script.py> output:
       EmployeeId  LastName FirstName       Title  ReportsTo  ... Country PostalCode              Phone                Fax                    Email
    0           6  Mitchell   Michael  IT Manager          1  ...  Canada    T3B 0C5  +1 (403) 246-9887  +1 (403) 246-9899  michael@chinookcorp.com
    1           7      King    Robert    IT Staff          6  ...  Canada    T1K 5N8  +1 (403) 456-9986  +1 (403) 456-8485   robert@chinookcorp.com
    2           8  Callahan     Laura    IT Staff          6  ...  Canada    T1H 1Y8  +1 (403) 467-3351  +1 (403) 467-8772    laura@chinookcorp.com
    
    [3 rows x 15 columns]
'''
