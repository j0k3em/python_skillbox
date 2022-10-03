N = int(input("Сколько будет чисел? "))
count = 0
for numbers in range(N):
    count_dividers = 0
    m = int(input("Число " + str(numbers + 1) + ": "))
    for numbers in range(1, m + 1):
        if m % numbers == 0:
            count_dividers += 1
    if count_dividers == 2:
        count += 1
print('Кол-во простых чисел в последовательности -', count)