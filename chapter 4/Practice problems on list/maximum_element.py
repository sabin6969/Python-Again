"""
Python program that takes a list of numbers and returns max number form it
"""


def maximum_number(nums):
    """
    This function accepts numbers and returns max number from it
    """
    highest = numbers[0]
    for i in range(1, len(nums)):
        if numbers[i] > highest:
            highest = numbers[i]
    return highest


def maximum_number2(nums):
    """
    Second approach to find maximum number
    """
    nums.sort()
    return nums[-1]


numbers = [33, 12, 45, 76, 101, 456]
print(maximum_number(numbers))
print(maximum_number2(numbers))
