inventory = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in inventory:
    frequency[item] = frequency.get(item, 0) + 1
print("Inventory count dictionary:")
print(frequency)