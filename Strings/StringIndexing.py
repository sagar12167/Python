# Indexing 
"""  
        It is Process of extracting Single Character at a time 
        from the Given String is called Indexing.

        Syntax : variable_name[ index_value ]

       -6 -5 -4 -3 -2 -1  <--- ( - Indexing Rigth tp Left)
        P  Y  T  H  O  N
        0  1  2  3  4  5  <--- ( + Indexing Left to Right)

"""

# Example 1 
language = "Python"

# + indexing left to right
print(language[0])  # p
print(language[1])  # y
print(language[4])  # o
print(language[3])  # H
print(language[5])  # n

# - indexing right to left 
print(language[-1])  # n 
print(language[-6],language[-3])  # p h
print(language[-2])  # o



# Example 2

"""
    +------------------------------------------------------------------------------------------------------------------------------------------+
    |   -23|-22 | -21 | -20 | -19 | -18 | -17 | -16 | -15 | -14 | -13 | -12 | -11 | -10 | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1   |   
    |------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------| 
    |   W  | e  |  l  |  c  |  o  |  m  |  e  |     |  t  |  o  |     |   p |  y  |  t  |  h  |  o  |  n  |     |  c  |  l  |  a  |  s  |  s   |
    |------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
    |   0  | 1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 |  15 |  16 |  17 |  18 |  19 |  20 |  21 |  22  |
    +------------------------------------------------------------------------------------------------------------------------------------------+
"""
print()
String = 'Wlecome to Python class'
print(len(String))
print()
print(type(String))

print(String[-10])
print(String[-20])