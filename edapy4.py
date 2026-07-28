names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))
print("Zipped List of Tuples:", combined)
print (combined)
for name, score in zip(names, scores):
    print(f"{name} scored {score} points.")