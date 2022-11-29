import math

horse_x = float(input('Введите расположение x коня: '))
horse_y = float(input('Введите расположение y коня: '))
horse_x = math.trunc(horse_x * 10)
horse_y = math.trunc(horse_y * 10)
needed_x = float(input('Введите желаемую x клетку: '))
needed_y = float(input('Введите желаемую y клетку: '))
needed_x = math.trunc(needed_x * 10)
needed_y = math.trunc(needed_y * 10)
print('Конь в клетке', (horse_x, horse_y), '.Точка в клетке', (needed_x, needed_y),'.')
if abs((horse_x - needed_x) * (horse_y - needed_y)) == 2:
	print('Да, конь может ходить в эту точку.')
else:
	print('Нет, конь не может ходить в эту точку.')

