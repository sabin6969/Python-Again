"""
Introduction to list
"""

# List is the collection of multiple elements seperated by comma and encolsed with square brackets
# Lists in python are ordered, mutable

names = ["Sabin", "Smith", "Raj", "Amit"]
print(names)
# append method adds one object at last of list
names.append("Padam")
print(names)
# extends method is used to extend list with iterable object
names.extend(["Biren", "Aryan", "Kissan"])
print(names)
# elements of list can be accessed using index
print(names[0])  # first element
print(names[0:3])  # 0 to 2
print(names[-1])  # last element
print(len(names))
