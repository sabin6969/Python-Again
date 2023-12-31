"""
A
A B
A B C
A B C D
A B C D E
"""

for row in range(1, 6):
    for cols in range(1, row+1):
        print(chr(64+cols), end=" ")
    print()
