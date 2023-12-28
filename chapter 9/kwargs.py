"""
**kwargs is a keyword argument passed to a function which accepts any length of key,value pair
kwargs are later treated as dictionary
"""


def details(**kwargs):
    print(kwargs)
    return


details(name="Sabin", age=20, address="Pokhara")

user_details = {
    "name": "Ram Kumar",
    "age": 19,
    "address": ["Rajkot", "Gujarat", "India"]
}
details(**user_details)  # ** means dictionary unpacking
