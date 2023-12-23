"""
Program to swap alternate elements of a list
for example 
input ->[1,2,7,8,5]
output ->[2,1,8,5]

input-->[1,2,7,8,5,6]
output ->[2,1,8,7,5,6]
"""


def swap_alternate(nums):
    print(f"Before swap {nums}")
    for i in range(0, len(nums), 2):
        j = i+1
        if not j >= len(nums):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
    print(f"After swap {nums}")


swap_alternate([1, 2, 3, 4, 5, 6])
