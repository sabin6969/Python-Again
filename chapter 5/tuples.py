"""
Tuple is a data structure which contains multiple elements seperated by comma and enclosed with parenthesis.
Tuples are immutable (they cannot be changed once initalized).
Tuples can contain duplicate value.
"""

# Syntax
names = ("Sabin", "Amit", "Padam", "Rajan", "Smith", "Sabin")
print(names)

# we can iterate through tuples
for i in names:
    print(i)


# tuples are faster than lists because of their immutable property

# syntax to declare tuple with only one element
numbers = (1,)  # (1) -->type is interger
