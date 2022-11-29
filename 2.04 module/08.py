import random
count_nums = int(input("Кол-во палок: "))
count_stones = int(input("Кол-во бросков: "))
while count_stones > count_nums:
    count_stones = int(input("Введите кол-во бросков < кол-во палок: "))
lucky = count_nums // count_stones
result = ""

nums_list = list(range(count_nums))
list_downed = ["." for _ in range(lucky + 1)]

for throw in range(count_stones):
    print(f"Бросок {throw + 1}.", end = " ")
    start = random.randint(1, count_nums - lucky)
    finish = start + lucky
    nums_list[start - 1:finish] = list_downed
    print(f"Сбиты палки от {start} по {finish}")

for sym in nums_list:
    if sym != ".":
        result += "I"
    else:
        result += "."

print()
print("Результат:", result)