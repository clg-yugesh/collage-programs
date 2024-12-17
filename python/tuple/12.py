tup = (0, 1, 2, 3, 4, 3, 5)

print("Tuple before removing : ",tup)

tup_list = list(tup)

tup_list.remove(2)

tup = tuple(tup_list)

print("Tuple after removing an element:", tup)