m = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]
print("Center element:", m[1][1])
flat = [item for row in m for item in row]
print("Flattened board:", flat)