"""
Program to calculate sum of natural numbers
"""
number = int(input("Enter a number: "))
total = 0
i = 1
while i <= number:
    total += i
    i += 1
print(total)
