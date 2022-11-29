def length():
    if len(pre_res) > len(input_user):
        finish = len(input_user)
    else:
        finish = len(pre_res)
    return finish

input_user = {"a": 1, "b": 2, "c": 3, "d": 4}

user_tuple = (10, 20, 30, 40)
pre_res = [elem for elem in input_user]
finish = length()

result = ((pre_res[count], user_tuple[count]) for count in range(finish))

print(f"Работа генератора в действии:\n",  result)
for elem in result:
    print(elem)