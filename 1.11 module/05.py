import math

earth_v = 10.8321 * 10 ** 11
radius = float(input('Введите радиус случайной планеты: '))
v = 4/3 * math.pi * radius ** 3
if v > earth_v:
	print('Объём планеты Земля меньше в', round((v / earth_v), 3), 'раз')
else:
	print('Объём планеты Земля больше в', round((earth_v / v), 3), 'раз')