"""
Function is the reusable block of code which is used to perform the specific task
"""
# function can be defined once and can be reused again and again
# function promotes code reusablity, maintainablity


def total(a, b):
    """
    total function takes two parameter a and b and returns its sum
    """
    return a+b


number1 = int(input("Enter a number: "))
number2 = int(input("Enter a another number: "))
print(total(number1, number2))
