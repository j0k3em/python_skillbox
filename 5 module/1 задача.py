expirience = int(input('Введите количество опыта: '))
if expirience >= 5000:
    level = 4
elif 2500 <= expirience < 5000:
    level = 3
elif expirience >= 1000:
    level = 2
else:
    level = 1
print('Ваш уровень:', level)
