text = input('Введите слово для Дешифрования: ')
counter = 0
first_part = ''
second_part = ''

for symbol in text:
  counter += 1
  if counter % 2 == 1:
    first_part += symbol
  else:
    second_part = symbol + second_part

print('Дешифрованное слово:', first_part + second_part)