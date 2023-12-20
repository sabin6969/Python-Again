"""
Python program to evaluate wheather a number is even or odd
"""


def odd_or_even(number):
    """
    takes a number as parameter. Returns True when number is even,False when number is odd
    """
    return number % 2 == 0


def is_even(number):
    """
    takes a number and returns even or odd string
    """
    ans = "Even" if number % 2 == 0 else "Odd"
    return ans


no = int(input("Enter a number: "))
result = odd_or_even(no)
if result:
    print("Even number")
else:
    print("Odd number")
