"""
List is the collection of multiple elements seperated by comma and enclosed with []
"""

# list methods
# methods to add element in a list
# append,extend,insert

# append
names = ["Sabin", "Padam"]
names.append("Smith")
names.append("Sandesh")
print(names)

# extend
names.extend(["Amit", "Kul Bahadur"])
print(names)

# insert
names.insert(0, "Sabin Dai")
print(names)

# methods to remove elements from list
# pop method by default removes at last
names.pop()  # removes element at last position by default
# pop also accepts index and removes that element from that index
names.pop(0)  # removes element at 0th index

# count
print(names.count("Sabin"))

# copy
# copys old element of a list into another list with different memory address
new_names = names.copy()
print(id(new_names))
print(id(names))
print(new_names)

# sort
# sort the elements of a list
names.sort()
print(names)

# reverse
names.reverse()
print(names)
