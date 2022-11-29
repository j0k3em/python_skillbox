max = 0
months = 122
ordered_numbers = True
for month in range(months):
    month = int(input('Введите зарплату: '))
    if month > max:
        max = month
    else:
        ordered_numbers = False
if ordered_numbers == True:
    print('Числа упорядочены')
else:
    print('Числа не упорядочены')