height = int(input('Введите высоту пирамиды: '))
raising = 1
 
for i in range(height):
  print(' ' * (height - 1 - i), '#' * raising, sep = '')
  raising += 2