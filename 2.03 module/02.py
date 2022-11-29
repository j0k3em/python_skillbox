first_class = list(range(160, 176 + 1, 2))
second_class = list(range(162, 180 + 1, 3))

first_class.extend(second_class)
first_class.sort()

print("Шеренга учеников", first_class)