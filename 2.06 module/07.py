orders = int(input("Введите кол-во заказов: "))
pizza_dict = dict()
for i_order in range(orders):
    print(f"{i_order + 1} заказ: ", end = "")
    order = input().split()
    while len(order) != 3:
        print("Введите правильно через пробел, фамилия название_пиццы колличество")
        print(f"{i_order + 1} заказ: ", end="")
        order = input().split()
    check = pizza_dict.get(f"{order[0]}")
    if check != None:
        last_check = pizza_dict.get(f"{order[0]}").get(f"{order[1]}")
        if last_check != None:
            pizza_dict[order[0]].update({order[1]: str(int(order[2]) + int(pizza_dict.get(f"{order[0]}").get(f"{order[1]}")))})
        else:
            pizza_dict[order[0]].update({order[1]: order[2]})
    else:
        pizza_dict[order[0]] = {order[1]: order[2]}

for key in pizza_dict:
    print(f"{key}:")
    for value in pizza_dict[key]:
        print("             ",
              f"{value}: {pizza_dict[key][value]}")