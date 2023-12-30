"""
*****
*****
*****
"""

"""
12345
12345
12345
12345
"""

"""
ABCDE
ABCDE
ABCDE
ABCDE   
"""


for row in range(1, 6, 1):
    for cols in range(1, 6, 1):
        print("*", end="")
    print("")

print("")

for row in range(1, 6, 1):
    for cols in range(1, 6, 1):
        print(cols, end="")
    print("")

print("")


for row in range(1, 6, 1):
    for cols in range(65, 70, 1):
        print(chr(cols), end="")
    print("")
