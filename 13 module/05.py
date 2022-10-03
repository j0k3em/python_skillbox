def get_number(quantitative, num_length):
  num = 0
  quantitive_info = 'Введите ' + quantitative + ' число: '
  while len(str(num)) != num_length:
    num = int(input(quantitive_info))
  return num
 
def change_num(num, num_length):
  last_digit = num % 10
  first_digit = num // 10 ** (num_length - 1)
  between_digits = num % 10 ** (num_length - 1) // 10
  num = last_digit * 10 ** (num_length - 1) + between_digits * 10 + first_digit
  return num
 
def get_first():
  num = get_number('первое (трёхзначное)', 3)
  num = change_num(num, 3)
  print('Изменённое первое число:', num)
  return num
 
def get_second():
  num = get_number('второе (четырёхзначное)', 4)
  num = change_num(num, 4)
  print('Изменённое второе число:', num)
  return num
 
first = get_first()
second = get_second()
 
print('Сумма чисел:', first + second)