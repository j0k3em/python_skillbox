def zip_func(first_block, second_block):
    first_block = list(first_block)
    second_block = list(second_block)
    a = [(first_block[i], second_block[i]) 
    for i in range(min(len(first_block), len(second_block)))]
    return a

string = "word"
tup = (10, 20, 30, 40)
print(zip_func(string, tup))

string = {1, 2, 3, 4}
tup = (10, 20, 30, 40)
print(zip_func(string, tup))