"""
Dictionary class methods

"""

user_data = {
    "name": "Sabin",
    "age": 20,
    "address": ["Pokhara,Nepal", "Ward no 19"],
}
print(id(user_data))
# accessing value through key
print(user_data.get("name"))
# or
print(user_data["name"])

# updating dictionary
additional_info = {
    "education": "Bachelor",
    "hobbies": ["Coding", "Building things"],
}
user_data.update(additional_info)
print(user_data)
print(id(user_data))

# accessing keys
print(user_data.keys())

# acessing values
print(user_data.values())


# items
print(user_data.items())

# another way to create dictionary
dct = dict(name="Another way", reason="practice")  # name and reasons are key
print(dct)
