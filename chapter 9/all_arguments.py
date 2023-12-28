"""
if we want to pass all kind of arguments to a function in python the order must be like this
1. positional parameter
2. *args
3. default parameter
4. **kwargs
"""


def all_type(positional, *args, default="default", **kwargs):
    print(positional)
    print(args)  # treated as tuple
    print(default)
    print(kwargs)  # treated as dictionary


all_type("Positional", 1, 2, 3, default="Default",
         name="Ram", age=20, address="Pokhara")
