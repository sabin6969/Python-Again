"""
Given a list of number return list having only even numbers
"""


def even_numbers(nums):
    """
    takes list (nums) and filters even numbers
    """
    even_numbers_list = []
    for num in nums:
        if num % 2 == 0:
            even_numbers_list.append(num)
    return even_numbers_list


def even_numbers_short_hand(nums):
    """
    Short hand (list compherension)
    """
    even_numbers_list = [i for i in nums if i % 2 == 0]
    return even_numbers_list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(numbers))
print(even_numbers_short_hand(numbers))
