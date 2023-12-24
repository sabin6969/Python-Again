# generating list from range function
# more on pop method
# index method
# passing list to a function

range_generated_function = list(range(1, 11))
print(range_generated_function)

# pop method returns poped items from a list
# pop method will remove last element by default
print(range_generated_function.pop())

# index method will return value error when searched element is not present in the collection we can even pass range


# passing list to a function
def negative_list(numbers):
    return [-i for i in numbers]


print(negative_list(range_generated_function))
