"""
F G H I J K
F G H I J K
F G H I J K
F G H I J K

"""

for rows in range(1, 6):
    for cols in range(1, 7, 1):
        print(chr(69+cols), end=" ")
    print()
