# Operations on Strings Methods

"""
       1. Updating a String :
            String cannot be changed directly after creation.
            So any modification in a new String being created using Slicing or medthods like replace().
"""
# Example of Updating a String

s = "SAMPATh"
s1 = s[:6]+"H" # Slicing Updating
print(s1)

s2 = s.replace("SAMPAT","sampat") # replace Method
print(s2)

print()
print("---------------------------------------------------")
print("Deleting a String")
print("---------------------------------------------------")

"""
        2. Deleting a String : 
            Individual string can not be delected became it is immutable.
            However, an entire string variable can be removed by using 'del' Keyword.
"""

# Example Deleting a String

print(f"Before Delecting : {s2}")
del s2
# print(f"After Delecting : {s2}")
print()

print("-------------------------------------")
print("Common String Methods")
print("-----------------------------------")

# Common String Methods
"""
        1. len()
        2. upper()
        3. lower()
        4. strip()
        5. replace()
"""

string1 = "Welcome to python class python"
length = len(string1) # length of the String1
upper = string1.upper() # It convert every characters in the String in Uppercase. 
lower = string1.lower() # It convert every characters in the string into lowerCase.
print(f"Length of the String is {length}")
print(f"Upper Case : {upper}")
print(f"Lower Case : {lower}")

string2 = " Hii, This is Sampath Sagar  "
split = string2.split() # It splits every word into list 
print(f"Removing the Space : {split}")

print(string1.capitalize()) # In the String First character will become Uppercase and remaining all will become lower Case. 
print(string1.casefold()) # It makes all the String into lower case. 
print(string1.count("python")) # It tell the count of repated word in the String
print(string1.endswith('python')) # It tell True/False when the character/word is ends with the same word/character it returns True. else False
print(string1.startswith("Wel")) # It tell True/False when the character/word is starts with the same character/word it returns True. else False
print(string1.find("")) # It find the character/word is present in string it return with index Starting value.if find("") is 0. if character/ word is not find default is -1. 
print("How Old are You {}".format(23)) 
print("my name is {}\nI'm {} is old".format("Sampath",23))
print(string1.index('s')) # It will find the charater/word of the Index Value.

string3 = 'Sampath637gmailcom'
# string3 = '35'
print(string3.isalnum()) # Returns True if all characters in the string are alphanumeric
print(string2.isalpha()) # Returns True if all characters in the string are in the alphabet
print(string3.isascii()) # Returns True if all characters in the string are ascii characters
print(string3.isdecimal()) # Returns True if all characters in the string are decimals
print(string3.isdigit()) # Returns True if all characters in the string are digits
# string3 = string3.lower()
# string3 = string3.upper()
print(string3.islower()) # Returns True if all characters in the string are lower case
print(string3.isupper()) #Returns True if all characters in the string are Upper case
print(string3.isidentifier()) # Returns True if the string is an identifier
# string1 = string1.title() # Converts the first character of each word to upper case
print(string1.istitle()) # Returns True if the string follows the rules of a title
print(string3.isspace()) # Returns True if all characters in the string are whitespaces
print(string3.rfind('g')) # Searches the string for a specified value and returns the last position of where it was found
print(string3.center(20)) # Returns a centered string

