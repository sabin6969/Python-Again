"""
Step argument in string slicing
by default step is 1
"""
# 0 to len with 1 step
# print("sabin"[::1])
# 0 to len with 2 step
print("Sabin"[::2])
# returns a empty string
print("Sabin"[5::2])
# -1 means in reverse order
# it is reverse String
print("Sabin"[len("Sabin")-1::-1])

print("Sabin"[::-1])
