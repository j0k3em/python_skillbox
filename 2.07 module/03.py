def tuple_return(tuple, elem):
    if elem not in tuple:
        return ()
    elif tuple.count(elem) == 1:
        print(tuple.count(elem))
        return tuple[tuple.index(elem):]
    elif tuple.count(elem) > 1:
        first_index = tuple.index(elem)
        final_index = (tuple.index(elem, first_index + 1)) + 1
        return tuple[first_index:final_index]

user_tuple = ("1", "2", "3", "4", "8", "7", "9", "i", "4", "d", "8", "7", "9", "i", "3", "4", "5")
elem = input("Введите элемент: ")

result = tuple_return(user_tuple, elem)
print(result, type(result))