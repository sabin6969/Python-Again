"""
Python program to find greatest number among two
"""


def greatest(num1, num2):
    """
    takes num1,num2 and returns the greatest among them
    """
    greatest_number = num1 if num1 > num2 else num2
    return greatest_number


highest_number = greatest(121, 22)
print(highest_number)
