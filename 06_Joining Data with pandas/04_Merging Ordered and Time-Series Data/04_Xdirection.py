'''
-> direction‘backward’ (default), ‘forward’, or ‘nearest’
----------------
left = pd.DataFrame({"a": [1, 5, 10], "left_val": ["a", "b", "c"]})
left.head()

    a left_val
0   1        a
1   5        b
2  10        c

right = pd.DataFrame({"a": [1, 2, 3, 6, 7], "right_val": [1, 2, 3, 6, 7]})
right.head()

   a  right_val
0  1          1
1  2          2
2  3          3
3  6          6
4  7          7
----------------
'''

pd.merge_asof(left, right, on='a')
'''
    a left_val  right_val
0   1        a          1
2  10        c          7
'''

pd.merge_asof(left, right, on='a', direction='forward')
'''
    a left_val  right_val
0   1        a        1.0
1   5        b        6.0
2  10        c        NaN
'''
pd.merge_asof(left, right, on='a', direction='nearest')
'''
    a left_val  right_val
0   1        a          1
1   5        b          6
2  10        c          7
'''
