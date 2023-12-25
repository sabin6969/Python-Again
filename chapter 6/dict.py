"""
Dictionary is the collection of key value pair enclosed with curly brackets
dictionary doesnot supports duplicate key
values of dictionary can be accessed using key
"""

user_info = {
    "name": "Sabin",
    "age": 20,
    "address": ["Pokhara", 19, 32000],

}
print(user_info)
print(user_info["name"])  # accessing value of name key
print(user_info.keys())  # returns keys
print(user_info.values())  # returns values
print(user_info.get("age"))  # accessing value of age key but error safe
user_info["newdata"] = "this is new data"
print(user_info)
print(len(user_info))
