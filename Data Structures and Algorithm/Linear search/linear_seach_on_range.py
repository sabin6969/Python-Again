"""
Python program to implement linear search on range of nums
"""


def linear_search_on_range(nums, start, stop, target):
    """
    this function takes nums,target,start and stop and performs linear search on that range
    """
    for i in range(start, stop+1):
        if nums[i] == target:
            return i
    return False


print(linear_search_on_range([12, 33, 45, 67, 871], 2, 4, 45))
