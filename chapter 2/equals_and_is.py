"""
in python == is used to check for equality that means == checks for value
is in python is used for identity check it checks for reference
"""
name = "Sabin"
name2 = "Sabin"
print(name == name2)  # == checks for value
print(name is name2)  # is checks for reference

# immutable objects having same value are stored in same memory space

lst = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst == lst2)  # true because value is same
print(lst is lst2)  # false because reference is different

# mutable objects having same values are stored in different memory location
