"""
1 4 9 16 25
1 4 9 16 25
1 4 9 16 25
1 4 9 16 25
"""

for rows in range(1, 6, 1):
    for cols in range(1, 6, 1):
        print(cols**2, end=" ")
    print()
