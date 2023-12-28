"""
*args is a parameter defined to a function which accepts any length of argument
args is later treated as tuple
"""


def total(*args):
    return sum(args)


# *args must be at last
def normal_and_args(normal, *args):
    print(type(normal))
    print(type(args))
    print(args)
    return


total(12, 32, 34, 45, 12)
normal_and_args(11, 45, "Sabin")

numbers = [22, 33, 12, 54, 66]
print(total(*numbers))  # * means list unpacking
print(total(numbers))  # will return an error
