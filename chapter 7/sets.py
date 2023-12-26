"""
Set is the collection of unique elements
they are unordered
they are mutable
sets are enclosed with curly brackets
"""

numbers = {1, 2, 3, 4, 5}
print(numbers)
# print(numbers[0]) returns an error
# sets are mutable
numbers.add(9)
# numbers.remove(10)   returns an error if not present
numbers.remove(3)  # removes 3 from set
numbers.discard(101)  # removes if present else will not return an error
