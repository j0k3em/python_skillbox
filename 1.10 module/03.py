width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))
line = ''
symbol =''
for row in range(1, height + 1):
    if row == 1 or row == height:
        symbol = '-'
    else:
        symbol = ' '
    line = '|' + (symbol * width) + '|'
    print(line)
