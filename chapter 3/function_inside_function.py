"""
Python program to call one function from another number
"""


def function1():
    """
    This is function1
    """
    print("This is function")


def another_function():
    """
    function which calls another function
    """
    function1()


another_function()
