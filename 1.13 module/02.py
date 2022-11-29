first_digit = int(input('Введите число: '))
second_digit = int(input('Введите число: '))
third_digit = int(input('Введите число: '))
 
def max_of_2(number_1, number_2):
    if number_1 > number_2:
        return number_1
    else:
        return number_2
 
print('Самое большое число:', max_of_2(max_of_2(first_digit, second_digit), third_digit))