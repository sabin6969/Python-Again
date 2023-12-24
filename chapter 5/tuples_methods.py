"""
Since tuples are immutable 
we cannot add,remove or insert element into it 
"""

# count
names = ("Sabin", "Ram", "Sabin", "Amit")
print(names.count("Sabin"))
print(names.count("Amit"))

# index
print(names.index("Sabin", 1))

numbers = tuple(range(10))  # 0 to 9

print(sum(numbers))
print(max(numbers))
print(min(numbers))

# len function
print("Length of tuple is {}".format(len(numbers)))
