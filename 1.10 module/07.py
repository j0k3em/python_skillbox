count_numbers = int(input('Введите количество чисел: '))
summ = 0
max_num = 0
max_sum = 0
 
for i in range(1, count_numbers + 1):
  query = 'Введите ' + str(i) + ' число: '
  number = int(input(query))
  backup_num = number
  while number > 0:
    summ += number % 10
    number //= 10
    if summ > max_sum:
      max_sum = summ
      max_num = backup_num
  summ = 0
 
print('Число', max_num, 'имеет максимальную сумму цифр:', max_sum)
