"""
Dictionary comprehension is a short hand syntax to generate dictionary in one line
"""

# cube dictionary
cube = {i: i**3 for i in range(1, 11)}
print(cube)

# odd even
odd_even = {i: ("even" if i % 2 == 0 else "odd")for i in range(1, 11)}
print(odd_even)
