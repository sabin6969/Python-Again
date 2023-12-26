# multiple keys having same values

user_info = dict.fromkeys(["name", "age", "address"], None)
print(user_info)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

user_info.update({
    "name": name,
    "age": age,
    "address": address
})
print(user_info)

# get method returns the value of coressponding key if not found return None
print(user_info.get("name"))
print(user_info.get("this key doesnot exist"))
print(user_info.get("asdfasf"), "Not found")

new_dict = user_info.copy()
print(id(new_dict))
print(id(user_info))
