count_of_containers = int(input("Кол-во контейнеров: "))
containers = []
for _ in range(count_of_containers):
    container = int(input("Введите вес контейнера: "))
    containers.append(container)
print()
new_containers = int(input("Введите вес нового контейнера: "))
for index in range(count_of_containers):
    if containers[index] >= new_containers:
        continue
    else:
        print("Номер, куда встанет новый контейнер:", index + 1)
        containers.insert(index, new_containers)
        break

print(containers)