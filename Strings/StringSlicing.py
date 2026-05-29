# String Slicing 

"""
        The process of extracting multiple characters together from the given String is called Slicing.
        Slicing can be done with help of index value based on start, End, and Step value.

        Syntax : 
                    variable_Name[ Start_Index : End_Index : Step_Index ]

                    1. The Default of Start_Index is 'Zero' .
                    2. The Default of End_Index is 'len(string)' .
                    3. The Default of Step_Index is 'One' . 

                    Step_Index:
                        i. Step value is 1 it doesn't skip any Characters.
                       ii. Step value is 2 it skip 1 character.
                      iii. Step value is 3 it skip 2 characters. etc...

"""

# Example 1

"""

    +-----------------------------------------------------+
    |  -9  |-8  | -7  | -6  | -5  | -4  | -3  | -2  | -1  |   
    |------|----|-----|-----|-----|-----|-----|-----|-----| 
    |   E  | d  |  u  |  c  |  a  |  t  |  i  |  o  |  n  |
    |------|----|-----|-----|-----|-----|-----|-----|-----|
    |   0  | 1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
    +-----------------------------------------------------+

"""
from ast import Str
string = 'Education'
print(string[::])
print(string[1:6])
print(string[-9])
print(string[-2::-2])
print(string[::-1])
print(string[-6:-4])

print()

# '+' Step_value Slicing 

print(string[::])  # Education
print(string[::1]) # Education
print(string[::2]) # Euain
print(string[::3]) # Eci
print(string[::4]) # Ean
print(string[::5]) # Et
print(string[::6]) # Ei
print(string[::7]) # Eo
print(string[::8]) # En
print(string[::9]) # E

print()

# '-' Step_vaue Slicing

print(string[::-1]) # noitacudE
print(string[::-2]) # niauE
print(string[::-3]) # ntu
print(string[::-4]) # naE
print(string[::-5]) # nc
print(string[::-6]) # nu
print(string[::-7]) # nd
print(string[::-8]) # nE
print(string[::-9]) # n

print()

# Start and Ending

print(string[0:9]) # Education
print(string[1:9]) # ducation
print(string[2:9]) # ucation
print(string[:2])  #Ed

print()

print(string[1:6]) # ducat
print(string[2:5]) # uca

print()

print(string[:-2]) # Educatio
print(string[3:-3]) # cat
print(string[-5:-2]) #ati

print()

# display auE
print(string[-5::-2]) # auE
# Display tu
print(string[-4:-8:-3]) # tu
# Display id
print(string[-3:-9:-5]) # id
# Display cation
print(string[-6:]) # cation
# Display ci
print(string[-6::3]) # ci
# Display Euain
print(string[::2]) #Euain

print(string[4:7]) # ati

print("----------------------------------------------")
# reverse the String
print(string[::-1])
print(string[-1:-10:-1])

# even and odd character in Forward Direction
print(string[::2])
print(string[1::2])

# Even and Odd Characters in Backward Direction
print(string[-2:-10:-2])
print(string[-2::-2])
print(string[-1:-10:-2])
print(string[-1::-2])


print()
print("-----------------------------------------------------------------------------------")

# Example 2

"""
    +------------------------------------------------------------------------------------------------------------------------------------------+
    |  -23 |-22 | -21 | -20 | -19 | -18 | -17 | -16 | -15 | -14 | -13 | -12 | -11 | -10 | -9  | -8  | -7  | -6  | -5  | -4  | -3  | -2  | -1   |   
    |------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------| 
    |   W  | e  |  l  |  c  |  o  |  m  |  e  |     |  t  |  o  |     |   p |  y  |  t  |  h  |  o  |  n  |     |  c  |  l  |  a  |  s  |  s   |
    |------|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
    |   0  | 1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 |  15 |  16 |  17 |  18 |  19 |  20 |  21 |  22  |
    +------------------------------------------------------------------------------------------------------------------------------------------+

"""

string2 = "Welcome to python class"

# Positive Slicing
print("Positive String Slicing")
print("---------------------------")
print(string2[0:7]) # Welcome
print(string2[8:10]) # to
print(string2[11:17]) # python
print(string2[18:23]) # class
print(string2[0:10]) # welcome to
print(string2[11:]) # Python class
print(string2[3:9]) # come t
print(string2[5:17]) # me to python
print(string2[:7]) # welcome
print(string2[8:]) # to python class

# Negative String Slicing

print("--------------------------------")
print("Negative String Slicing")
print("--------------------------------")
print()
print(string2[-5::]) # class
print(string2[-12:-6]) # python
print(string2[-23:-16]) # Welcome
print(string2[-15:-13]) # to
print(string2[-11:-6]) # ytho
print(string2[-23:]) # Welcome to python class
print(string2[-23:-5]) # Welcome to python
print(string2[-5:]) # class
print(string2[-10:-5]) # thon
print()

# Reversing String Slicing

print("--------------------------------")
print("Revesing String Slicing")
print("--------------------------------")
print()
print(string2[::-1]) # Welcome to python class
print(string2[22::-1]) 
print(string2[16:10:-1]) # nohtyp
print(string2[-1:-6:-1]) # ssalc
print(string2[9::-1]) # ot emocleW
print(string2[6::-1]) # emocleW