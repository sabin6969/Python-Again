"""
even_numbers_of_digits2 is more effective and optimized
because in even_numbers_of_digit a new list is created while in another function new list is not created
"""


def even_numbers_of_digits(nums):
    return len([i for i in nums if len(str(i)) % 2 == 0])


def even_numbers_of_digits2(nums):
    count = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            count += 1
    return count


nums = [12, 345, 2, 6, 7896]
print(even_numbers_of_digits(nums))
print(even_numbers_of_digits2(nums))
