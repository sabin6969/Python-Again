"""
Lists inside tuple
Tuple unpacking
"""

# we can change list inside tuple
names = (["Sabin", "Ram", "Amit"],)  # tuples with only one element
print(names)
names[0][1] = "Smith"
print(names)


# tuple unpacking

goals = (2, 3, 1, 5)
smit, ram, amit, biren = goals
print(smit)
print(ram)
print(biren)
print(amit)
