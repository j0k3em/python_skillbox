def calc():
    while True:
        number = int(input('Введите число(0 - выход): '))
        if number == 0:
            break
        operation = int(input('Выберите действие:\n'
                              '1 - Вывести сумму цифр\n'
                              '2 - Вывести максимальную цифру\n'
                              '3 - Вывести минимальную цифру\n'))

        if operation == 1:
            sum_nums(number)
        if operation == 2:
            max_num(number)
        if operation == 3:
            min_num(number)

def sum_nums(number):
    suma = 0
    while number > 0:
        digit = number % 10
        suma = suma + digit
        number = number // 10
    print("Сумма:", suma)

def max_num(number):
    max = 0
    while number > 0:
        digit = number % 10
        if digit > max:
            max = digit
        number = number // 10
    print('Наибольшее число =', max)

def min_num(number):
    min = 9
    while number > 0:
        digit = number % 10
        if min > digit:
            min = digit
        number = number // 10
    print('Наименьшее число =', min)

calc()