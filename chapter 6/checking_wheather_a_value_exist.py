user_info = {
    "name": "Sabin Poudel",
    "age": 20,
    "address": ["Pokhara", 19]
}
if user_info.get("namewa"):  # if key doesnot exist it will return None which means false
    print("Found")
else:
    print("Not found")
