'''
03 - Importing non-flat files from the web

Congrats! You've just loaded a flat file from  the web  into  a  DataFrame  without  first 
saving it locally using the pandas function pd.read_csv(). This  function  is  super  cool 
because it has close relatives that allow you to load  all types of files, not  only  flat 
ones. In this interactive exercise, you'll use pd.read_excel() to import an Excel spreadsheet.

The URL of the spreadsheet is

'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

Your job is to use pd.read_excel() to read in all of its sheets, print the sheet names and then print 
the head of the first sheet using its name, not its index.

Note that the output of pd.read_excel() is a Python dictionary with sheet names as keys and corresponding
 DataFrames as corresponding values.

Instructions:

- Assign the URL of the file to the variable url.
- Read the file in url into a dictionary xls using pd.read_excel() recalling that, in order to import all 
  sheets you need to pass None to the argument sheet_name.
- Print the names of the sheets in the Excel spreadsheet; these will be the keys of the dictionary xls.
- Print the head of the first sheet using the sheet name, not the index of the sheet! The sheet name is '1700'
'''
# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
df_xls = pd.read_excel(url, sheetname=None)

# Print the sheetnames to the shell
print(df_xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(df_xls['1700'].head())
