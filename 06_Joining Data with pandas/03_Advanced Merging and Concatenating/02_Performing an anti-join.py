'''
02 - Performing an anti-join

In our music streaming company dataset, each customer is assigned an employee 
representative to assist them. In this exercise, filter the employee table by 
a table of top customers, returning only those employees who are not assigned 
to a customer. The results should resemble the results of  an  anti-join.  The 
company's leadership will assign these employees additional training  so  that 
they can work with high valued customers.

The top_cust and employees tables have been provided for you.
-----------------------------------------------------------------------------------------------------
top_cust.head()

   cid  srid      fname        lname               phone                 fax                     email
0    1     3       Luís    Gonçalves  +55 (12) 3923-5555  +55 (12) 3923-5566      luisg@embraer.com.br
1    2     5     Leonie       Köhler    +49 0711 2842222                 NaN     leonekohler@surfeu.de
2    3     3   François     Tremblay   +1 (514) 721-4711                 NaN       ftremblay@gmail.com
3    4     4      Bjørn       Hansen     +47 22 44 22 22                 NaN     bjorn.hansen@yahoo.no
4    5     4  František  Wichterlová    +420 2 4172 5555    +420 2 4172 5555  frantisekw@jetbrains.com
employees.head()

   srid    lname     fname                title  hire_date                     email
0     1    Adams    Andrew      General Manager 2002-08-14    andrew@chinookcorp.com
1     2  Edwards     Nancy        Sales Manager 2002-05-01     nancy@chinookcorp.com
2     3  Peacock      Jane  Sales Support Agent 2002-04-01      jane@chinookcorp.com
3     4     Park  Margaret  Sales Support Agent 2003-05-03  margaret@chinookcorp.com
4     5  Johnson     Steve  Sales Support Agent 2003-10-17     steve@chinookcorp.com
--------------------------------------------------------------------------------------------------------

Instructions:

1. Merge employees and top_cust with a left join, setting indicator argument to True. 
   Save the result to empl_cust.

'''
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)


'''
2. Select the srid column of empl_cust and the rows where _merge is 'left_only'. Save the 
   result to srid_list.
'''
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']


'''
3. Subset the employees table and select  those  rows  where  the srid is  in  the  variable  
   srid_list and print the results.
'''
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])
