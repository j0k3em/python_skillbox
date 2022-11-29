height = int(input('Укажите высоту ямы: '))
row = height - 1
print()
 
while row >= 0:
  for i in range(-height, height + 1):
    if abs(i) > row:
      print(abs(i), end = '')
    elif i == 0:
      print(end = '')
    else:
      print('.', end = '')
  row -= 1
  print()