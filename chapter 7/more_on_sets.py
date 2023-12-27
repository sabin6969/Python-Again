"""
More on sets
| -->union operator
& -->intersection operator
"""
names1 = {"Sabin", "Amit", "Smith", "Kul"}
names2 = {"Amit", "Biren", "Padam"}
union = names1 | names2
intersection = names1 & names2
print(union)
print(intersection)

# we cannot add list ,dictionary, tuples inside

new_set = {["Sabin", "poude"], "Biren"}  # will give an error
print(new_set)

# we can even use copy and clear method on set objects
