"""
Python program that returns last character of name
"""


def last_character(name):
    """
    This function takes name as parameter and rerturns its last character
    """
    if name:
        # return name[len(name)-1]
        # or
        return name[-1]
    return "Empty string provided"


print(last_character("Sabin"))
