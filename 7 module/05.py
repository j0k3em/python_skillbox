answer = 1
your_number = int(input('Введите число: '))
for number in range(1, your_number + 1):
    answer *= number
print('Факториал числа', your_number, 'равен', answer)