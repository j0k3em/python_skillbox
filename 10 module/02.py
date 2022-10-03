N = int(input('Введите число: '))
line = ''
for row in range(N + 1):
  line = str(row) + '\t'
  print(line * row)