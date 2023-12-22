"""
Python program to find sum of elements of a list
"""


def total(numbers):
    """
    This function takes a list and returns sum of elemets of a list
    """
    add = 0
    for number in numbers:
        add += number
    return add


addition = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(addition)
