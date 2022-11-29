videocards = int (input("Кол-во видеокарт: "))
videocards_base = []
new_base = []
for number in range(videocards):
    print(number + 1, "Видеокарта: ", end = "")
    name = int(input())
    videocards_base.append(name)
result = videocards_base[0]
for index in range(videocards):
    if result < videocards_base[index]:
        result = videocards_base[index]

for index in range(videocards):
    if videocards_base[index] != result:
        new_base.append(videocards_base[index])
print("Старый список видеокарт: ", videocards_base)
print("Новый список видеокарт: ", new_base)