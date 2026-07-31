products = [("Laptop", 1200), ("Mouse", 25), ("Monitor", 300), ("Keyboard", 75)]
products.sort(key=lambda product: product[1])
print("Products sorted by price (ascending):")
print(products)