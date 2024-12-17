tup1 = (1, 2, 3, 4)
tup2 = (3, 4, 5, 6)

print(tup1)
print(tup2)

common = tuple(set(tup1) & set(tup2))

print("Common elements:", common)