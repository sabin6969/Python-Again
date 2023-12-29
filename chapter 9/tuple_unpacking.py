"""
Tuple packing and unpacking
"""
# multiple values one variable tuple packing
names = "Sabin", "Ram", "Amit", "Biren"
print(names)

# one value multiple variables
# tuple unpacking
red, orange, *other = ("Apple", "Orange", "Gava", "Banana")
print(red)
print(orange)
print(other)
