# String
"""
        String is a Collection of the Characters. enclosed with [ ' ', " ", ''' ''', """ """].
            1. It is an Immutable data type. [it can not modify]
            2. We can perform indexing and Slicing on String.
            3. It allows Duplicates.
"""

name = input("Enter the Your Name : ")
print(f"Hello {name}")

# Write a Program to calculate Number of Characters Present in a given String

s1 = "Welcome to Python"
print(f"Number of Characters Present in String is {len(s1)}")

# 4. If any modification to a string creates a new String instead of altering the orginal one .
s = 'SAMPATh'
s = s[:6]+'H'
print(s)


del s1

# Format String
age = 23
name = 'Sampath Sagar'
msg = f"My Name is {name}, I am {age}"
print(msg)
Bill = 452.69
msg = f"The Current Bill is ₹ {Bill:.1f}"
print(msg)
