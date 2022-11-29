videocards = int (input("Кол-во видеокарт: "))
old_base = []
new_base = []
for number in range(videocards):
    print(number + 1, "Видеокарта: ", end = "")
    name = int(input())
    old_base.append(name)
result = old_base[0]
for i in range(videocards):
    if result < old_base[i]:
        result = old_base[i]

for i in range(videocards):
    if old_base[i] != result:
        new_base.append(old_base[i])
print("Старый список видеокарт: ", old_base)
print("Новый список видеокарт: ", new_base)