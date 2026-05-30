# List 
"""
    List :
            It is collection of Hemogenous and Hetrogenous elements seprated by comma and enclosed with square brackets '[]'.
           
             Homogenous : Same datatype values is called Homogenous. 
                          Ex: [10, 20, 40, 50]

            Hetrogenous : Different Datatype values is called Hetrogenous. 
                          Ex: [20, 16.54, 16+3j, 'Sam', (20,30,50), {30,56}]
        
            1. List should enclosed with '[]'.
            2. It allows Dupilcate values. Ex: [10,60,20,60]
            3. It is an Mutable (Its can modify,add,remove the elements in the list).
            4. It allows int, float, char, str, complex, bool, tuple, set, dict, and list.
            5. Any item from the list can be accessed using its index, and can be modified.
            6. Ordered: elements maintain the order in which they are inserted.
"""

list1 = [10 ,20, 30, 40]
print(list1)

# user input
user = list(input("Enter the list: ").split())
print(user)

# User input using map function
User = list(map(int,input("Enter the list: ").split()))
print(User)

