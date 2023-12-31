"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
"""

for row in range(1, 7):
    for cols in range(1, row+1):
        print(cols, end=" ")
    print()
else:
    for i in range(1, 7):
        print(i, end=" ")
