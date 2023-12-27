"""
Short hand syntax to generate sets 
sets are unordered
we cannot access elements of sets using index 
"""

names = ["Sabin", "Rohan", "Smith", "Pappu", "Ava", "Bnu"]
first_character_set = {i[0] for i in names if len(i) > 3}
print(first_character_set)
