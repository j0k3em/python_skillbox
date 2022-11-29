shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_sorted = input("Название детали: ")

count_detail = 0
cost = 0
count = len(shop)

for i_count in range(count):
        if shop[i_count][0] == name_sorted:
                count_detail += 1
                cost += shop[i_count][1]

print()
print("Кол-во деталей   -", count_detail)
print("Общая стоимость -", cost)