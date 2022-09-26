number = int(input('Введите число: '))
if (10 <= number <= 99) or (-99 <= number <= -10):
    print('Число', number, 'двузначное')
else:
    print('Число', number, 'не двузначное')
