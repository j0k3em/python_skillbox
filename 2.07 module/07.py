def is_float(tuple):
    not_true = False
    for element in tuple:
        if type(element) == float:
            return True

new_tuple = (122, 126, 1.22, 161, 166, -16, 1, -14, 70, 75, 81, 88, 121, 167, 173, 182, 188, 200, 271, 279, 292, 298)

if is_float(new_tuple):
    print("Результат:", end = " ")
    print(new_tuple)
else:
    print("Результат:", end=" ")
    print(tuple(sorted(new_tuple)))