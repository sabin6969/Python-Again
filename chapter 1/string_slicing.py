"""
String slicing is the process of retriving part of a String
"""
NAME = "Sabin"
# 0,1,2
# Start 0 (inclusive)
# End 3 (exclusive)
print(NAME[0:3])
# without any index
# entire string will be printed
print(NAME[:])

# with start index only
# characters after index 1 will be printed
print(NAME[1:])

# with stop index only
# start to 3 only will be printed
print(NAME[:4])
