text = input("Введите строку: ")
set_text = set(text)
count_result = 0

for i_sym in set_text:
    count = 0
    for sym in text:
        if i_sym in sym:
            count += 1
    if count % 2 != 0:
        count_result += 1

if count_result < 2:
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")