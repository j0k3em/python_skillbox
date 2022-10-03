from re import M


a = float(input('Введите начальную амплитуду: '))
b = float(input('Введите амплитуду остановки: '))
m = 0.916
count = 0
while  a > b:
    a *= m 
    count += 1
print('Маятник считается остановившимся через', count, 'колебаний')