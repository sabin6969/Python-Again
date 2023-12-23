"""
Python program to find minimum number from an array
"""


class Minimum:
    """
    class to find minimum number
    """
    nums = []

    def __init__(self, numbers):
        self.nums = numbers

    def method1(self):
        """
        iterative method
        """
        minimim = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] < minimim:
                minimim = self.nums[i]
        return minimim

    def method2(self):
        """
        very short line but time consuming
        """
        minumum = sorted(self.nums)[0]
        return minumum


m = Minimum([12, 33, 44, 561, -3])
print(m.method1())
print(m.method2())
