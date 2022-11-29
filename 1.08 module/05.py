start = int(input('Начало:'))
stop = int(input('Конец:'))
step = int(input('Шаг:'))
if stop > start:
	start, stop = stop, start
if step > 0:
	step -= abs(step) * 2
for x in range(start, stop - 1, step):
	y = x ** 3 + 2 * x ** 2 - 4 * x + 1
	print('В точке', x, 'функция равна', y)