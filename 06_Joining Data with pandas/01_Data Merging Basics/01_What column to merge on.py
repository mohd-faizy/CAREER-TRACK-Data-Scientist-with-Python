'''
01_What column to merge on?

Chicago provides a list of taxicab owners and  vehicles  licensed  to  operate  within  the
city, for public safety. Your goal is to merge two tables  together. One  table  is  called
taxi_owners, with info about the taxi cab company owners, and one is called taxi_veh,  with
info about each taxi cab vehicle. Both the taxi_owners and taxi_veh tables have been loaded
for you and you can explore them in the console.

-------------------------------------------------------------
taxi_owners.head()
Out[1]:

     rid   vid           owner                 address    zip
0  T6285  6285  AGEAN TAXI LLC     4536 N. ELSTON AVE.  60630
1  T4862  4862    MANGIB CORP.  5717 N. WASHTENAW AVE.  60659
2  T1495  1495   FUNRIDE, INC.     3351 W. ADDISON ST.  60618
3  T4231  4231    ALQUSH CORP.   6611 N. CAMPBELL AVE.  60645
4  T5971  5971  EUNIFFORD INC.     3351 W. ADDISON ST.  60618
In [2]:
taxi_veh.head()
Out[2]:

    vid    make   model  year fuel_type                owner
0  2767  TOYOTA   CAMRY  2013    HYBRID       SEYED M. BADRI
1  1411  TOYOTA    RAV4  2017    HYBRID          DESZY CORP.
2  6500  NISSAN  SENTRA  2019  GASOLINE       AGAPH CAB CORP
3  2746  TOYOTA   CAMRY  2013    HYBRID  MIDWEST CAB CO, INC
4  5922  TOYOTA   CAMRY  2013    HYBRID       SUMETTI CAB CO

------------------------------------------------------------
Choose the column you would use to merge the two tables on using the .merge() method.

-> on='vid'
'''
