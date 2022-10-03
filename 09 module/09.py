phrase = input('Введите строку: ')
milk_in_seat = 0
milk_sum = 0

for seat in phrase:
    milk_in_seat +=2
    if milk_in_seat > 20:
        break
    elif seat == 'b':
        milk_sum += milk_in_seat

print('Общий объем молока: ', milk_sum)