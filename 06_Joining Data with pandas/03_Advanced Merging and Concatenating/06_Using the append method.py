'''
06 - Using the append method

The .concat() method is excellent when you  need a  lot  of  control over 
how concatenation is performed. However, if you  do  not  need   as  much 
control, then the .append() method  is another  option. You'll try   this  
method out by appending the track lists together from different Metallica 
albums. From there, you will merge it  with the  invoice_items  table  to 
determine which track sold the most.

The tables tracks_master, tracks_ride, tracks_st, and  invoice_items  have
loaded for you.
---------------------------------------------------------------------------
tracks_master.head()
---------------------------------------------------------------------------
    tid               name  aid  mtid  gid             composer  u_price
0  1853            Battery  152     1    3  J.Hetfield/L.Ulrich     0.99
1  1854  Master Of Puppets  152     1    3            K.Hammett     0.99
4  1857  Disposable Heroes  152     1    3  J.Hetfield/L.Ulrich     0.99


---------------------------------------------------------------------------
tracks_rid.head()
---------------------------------------------------------------------------
    tid                     name  aid  mtid  gid  u_price
0  1874     Fight Fire With Fire  154     1    3     0.99
1  1875       Ride The Lightning  154     1    3     0.99
2  1876  For Whom The Bell Tolls  154     1    3     0.99
3  1877            Fade To Black  154     1    3     0.99
4  1878        Trapped Under Ice  154     1    3     0.99


---------------------------------------------------------------------------
tracks_st.head()
---------------------------------------------------------------------------
    tid                  name  aid  mtid  gid  u_price
0  1882               Frantic  155     1    3     0.99
1  1883             St. Anger  155     1    3     0.99
2  1884  Some Kind Of Monster  155     1    3     0.99
3  1885          Dirty Window  155     1    3     0.99
4  1886         Invisible Kid  155     1    3     0.99


---------------------------------------------------------------------------
invoice_items.head()
---------------------------------------------------------------------------
   ilid  iid  tid  uprice  quantity
0     1    1    2    0.99         1
1     2    1    4    0.99         1
2     3    2    6    0.99         1
3     4    2    8    0.99         1
4     5    2   10    0.99         1
---------------------------------------------------------------------------

Instructions:

- Use the .append() method to combine (in this order)tracks_ride, tracks_master,
  and tracks_st together vertically, and save to metallica_tracks.

- Merge metallica_tracks and invoice_items on tid with an inner join, and save to 
  tracks_invoices.

- For each tid and name in tracks_invoices, sum the quantity sold column, and save
  as tracks_sold.

- Sort tracks_sold in descending order by the quantity column, and print the table.
'''
# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid', 'name']).agg({'quantity': 'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(['quantity'], ascending=False))
