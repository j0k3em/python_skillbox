import math
 
megabytes = int(input('Укажите размер файла: '))
speed = int(input('Какова скорость вашего соединения? '))
second = 1
for mb in range(speed, megabytes, speed): 
  print('Прошло', second, 'сек. Скачано', mb, 'из', megabytes, 'Мб','(', math.trunc(speed * second / megabytes * 100), ')%')
  second += 1
else:
    print('Прошло', second, 'сек. Скачано', megabytes, 'из', megabytes, 'Мб','(', 100, ')%')

	
	