height = int(input('Количество уровней пирамиды: '))
number = 1
 
for row in range(1, height + 1):
  print('\t' * (height - row), end = '')
  for col in range(row):
    print(number, end = '')
    number += 2
    print('\t' * 2, end = '')
  print()