"""
Program to search element in 2d array
"""


def search_in_2d_list(numbers, target):
    """
    Searching for element in 2d lists 
    """
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] == target:
                return f"{i} {j}"
    return False


nums = [
    [12, 33, 45],
    [33, 56, 91],
    [56, 87, 91],
]
print(search_in_2d_list(nums, 333))
