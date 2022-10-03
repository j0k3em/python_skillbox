width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))
for row in range(width + 1):
  for col in range(height + 1):
    if col == row:
      print('^', end='')
    elif col == - row + (width - 1):
      print('^', end='')
    else:
      print(' ', end='')
  print()