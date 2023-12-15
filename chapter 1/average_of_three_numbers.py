"""
Average of three numbers
"""
no1, no2, no3 = input("Enter three numbers seperated by comma: ").split(",")
print(
    f"Average of {no1},{no2},{no3} is {round((int(no1)+int(no2)+int(no3))/3,2)}")
