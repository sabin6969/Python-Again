"""
Python program to implement linear search 
"""


def linear_search(nums, target):
    """
    This function will take nums and target and returns if target is present in nums else returns False
    """
    # iterating through nums
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return False


NUMS = [12, 33, 56, 71, 89]
INDEX = linear_search(NUMS, 89)
print(INDEX)
