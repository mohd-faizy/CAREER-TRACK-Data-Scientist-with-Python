'''
04 - Concatenation basics

You have been given a few tables of data with  musical  track  info  for 
different albums from the metal band, Metallica. The  track  info  comes 
from their Ride The Lightning, Master Of Puppets, and St. Anger  albums. 
Try various features of the .concat() method by concatenating the tables 
vertically together in different ways.

The tables tracks_master, tracks_ride, and tracks_st have loaded for you.
------------------------------------------------------------------------
tracks_master.head()

    tid               name  aid  mtid  gid             composer  u_price
0  1853            Battery  152     1    3  J.Hetfield/L.Ulrich     0.99
1  1854  Master Of Puppets  152     1    3            K.Hammett     0.99
4  1857  Disposable Heroes  152     1    3  J.Hetfield/L.Ulrich     0.99

tracks_ride.head()

    tid                     name  aid  mtid  gid  u_price
0  1874     Fight Fire With Fire  154     1    3     0.99
1  1875       Ride The Lightning  154     1    3     0.99
2  1876  For Whom The Bell Tolls  154     1    3     0.99
3  1877            Fade To Black  154     1    3     0.99
4  1878        Trapped Under Ice  154     1    3     0.99

tracks_st.head()

    tid                  name  aid  mtid  gid  u_price
0  1882               Frantic  155     1    3     0.99
1  1883             St. Anger  155     1    3     0.99
2  1884  Some Kind Of Monster  155     1    3     0.99
3  1885          Dirty Window  155     1    3     0.99
4  1886         Invisible Kid  155     1    3     0.99

-----------------------------------------------------------------------

Instructions:

1. Concatenate tracks_master, tracks_ride, and tracks_st, in that order, setting
   sort to True.
'''
# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort=True)
print(tracks_from_albums)
'''
2. Concatenate tracks_master, tracks_ride, and tracks_st, where the index goes from 
   0 to n-1.
'''
# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)
'''
3. Concatenate tracks_master, tracks_ride, and tracks_st, showing only columns that 
   are in all tables.
'''
# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)
