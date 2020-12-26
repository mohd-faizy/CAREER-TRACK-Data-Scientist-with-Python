'''
03 - Performing a semi-join

Some of the tracks that have generated the most significant  amount  of
revenue are from TV-shows or are other non-musical audio. You have been 
given a table of invoices that  include  top  revenue-generating  items. 
Additionally, you have a table of non-musical tracks from the streaming 
service. In this exercise, you'll use a semi-join to find the top revenue-
generating non-musical tracks..

The tables non_mus_tcks, top_invoices, and genres have been loaded for you.

---------------------------------------------------------------------------
non_mus_tcks.head()

       tid                    name  aid  mtid  gid  u_price
2819  2820  Occupation / Precipice  227     3   19     1.99
2820  2821           Exodus, Pt. 1  227     3   19     1.99
2821  2822           Exodus, Pt. 2  227     3   19     1.99
2822  2823           Collaborators  227     3   19     1.99
2823  2824                    Torn  227     3   19     1.99

top_invoices.head()

     ilid  iid   tid  uprice  quantity
469   470   88  2832    1.99         1
472   473   88  2850    1.99         1
475   476   88  2868    1.99         1
526   527   96  3214    1.99         1
527   528   96  3223    1.99         1

genres.head()

   gid                name
0    1                Rock
1    2                Jazz
2    3               Metal
3    4  Alternative & Punk
4    5       Rock And Roll
---------------------------------------------------------------------------

Instructions:

- Merge non_mus_tcks and top_invoices on tid using an inner join. Save the 
  result as tracks_invoices.

- Use .isin() to subset the rows of non_mus_tck where tid is in the tid column 
  of tracks_invoices. Save the result as top_tracks.

- Group top_tracks by gid and count the tid rows. Save the result to cnt_by_gid.

- Merge cnt_by_gid with the genres table on gid and print the result.
'''
# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcsk to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid': 'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
