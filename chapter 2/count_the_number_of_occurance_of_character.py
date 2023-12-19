"""
Program to count the no of occurance of char in strings
Sabin Paudel
S->1
a->2
b->1
i->1
n->1
P->1
u->1
d->1
e->1
l->1
"""
name = input("Enter your name: ")
already_occured_character = ""
i = 0
while i < len(name):
    if name[i] not in already_occured_character:
        print(f"{name[i]}-->{name.count(name[i])}")
        already_occured_character += name[i]
    i += 1
