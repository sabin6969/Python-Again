"""
Python program to concat two strings
"""


def full_name(first_name, last_name):
    """
    takes two parameter as first_name and last_name and returns its concat with space in between
    """
    return f"{first_name} {last_name}".title()
    # return first_name+" "+last_name


fname = input("Ener your firstname: ")
lname = input("Enter your lastname: ")
name = full_name(fname, lname)
print(name)
