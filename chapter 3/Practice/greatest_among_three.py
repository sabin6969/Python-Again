"""
Program to find greatest number from 3 numbers
"""


def greatest(a, b):
    """
    this function takes two parameter a and b. returns greatest among them
    """
    return a if a > b else b


def greatest_among_three(a, b, c):
    """
    this function takes three parametr a, b and c and returns greatest among them
    """
    return greatest(greatest(a, b), c)


largest_number = greatest_among_three(12, 32, 321)
print(largest_number)
