def dir(info):
    info = {'name':"hamza", 'age':18, "nation":'Pakistan',"education":'ICS'}
    # this is a dictionary and i dont know what kind of and how many method i can use in this dict.
    # So, I can see all it method by running follwing line of code
    print("\n-----All Methods of Dictionary-----\n")
    print(info.__dir__())
    #  If i want to know which type of method DIR is i can check it via this command
    print("\n-----Method type of dir-----\n")
    print(info.__dir__)

def dict():
    print("\nDICT ATTRIBUTE\n")

    from dataclasses import dataclass
    @dataclass
    class Human:
        name = "Hamza"
        age  = 18
        education = 'ICS'

    # Now if i will use dict attribute it will wrap my all info of class in a dict
    print("\n-----Output of Dict Attribute-----\n")
    hamza = Human
    print(hamza.__dict__) # It is shoowing other things as well because we use dataclass decorator which creates some func automatically if we will not use it it will only display a dict
    #  You can try it without using a dataclass decorator

def help(info):
    info = {'name':"hamza", 'age':18, "nation":'Pakistan',"education":'ICS'}
    print("\nHELP METHOD\n")
    # This is one of the most usefull method by using this method we can get details about any method or data type or anything in python
    #  It work as a short hand python documentation if you donot want to go to browser to see documentation you can use help method to get a short intro about any datatype or func

    print("-----OUtput of Help Method------\n")
    # Syntax of help function is as follows
    print(help(info))

try:
    inp = input("Which thing you want to go thorugh (dir, dict or help): ").lower()
    if inp == 'dir':
       dir()
    elif inp == 'dict':
        dict()
    elif inp == 'help':
        help()
    else:
        print("Invalid input! Please enter 'dir', 'dict', or 'help'.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("\nThank you for using this script! If you have any questions, feel free to ask.")
# This script demonstrates the use of dir, dict, and help methods in Python.