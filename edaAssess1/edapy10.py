grocery_list = ["Milk", "Eggs", "Bread", "Butter"]
print("Your Shopping List:")
for index, item in enumerate(grocery_list, start=1):
    print(f"{index}. {item}")