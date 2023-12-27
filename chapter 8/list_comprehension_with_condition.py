"""
List comrehension with if else statement
"""

# generate a lists of numbers
# double if even
# square if odd

double_square = [i*2 if i % 2 == 0 else i**2 for i in range(1, 11)]
print(double_square)

odd_even = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(odd_even)


# first character of a name
names = ["Sabin", "Kule", "Padam", "Sandesh", "Santo", "Amit"]

only_first_character = [i[0] for i in names]
print(only_first_character)
