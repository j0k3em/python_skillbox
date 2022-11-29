first_side = int(input('Введите размер стороны листа: '))
second_side = first_side
evelope = 12
count = 0
while evelope < first_side or evelope < second_side:
    if evelope < first_side:
        count += 1
        first_side = first_side / 2
        if evelope < second_side:
            count += 1
            second_side = second_side / 2
print('Складывать ', count, 'раз')
