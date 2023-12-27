"""
List comprehension is a short hand syntax to generate a list based on certain condition.
"""

# create a list of numbers from 1 to 10
number = [i for i in range(1, 11)]
print(number)


# create a list of square of numbers from 1 to 10

# old method
square_number = []
for i in range(1, 11):
    square_number.append(i**2)
print(square_number)


# short method
square_number_new = [i**2 for i in range(1, 11)]
print(square_number_new)


cube_numbers = [i**3 for i in range(1, 11)]
print(cube_numbers)
