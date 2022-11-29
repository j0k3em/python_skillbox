main = [1, 5, 3]
second = [1, 5, 1, 5]
third = [1, 3, 1, 5, 3, 3]

main.extend(second)

print("Кол-во цифр 5 при первом объединении:", main.count(5))
for index in main:
    if index == 5:
        main.remove(index)

main.extend(third)

print("Итоговый список", main)