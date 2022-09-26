firstVar = int(input('Введите первую переменную: '))
secondVar = int(input('Введите вторую переменную: '))
thirdVar = int(input('Введите третью переменную: '))
if firstVar > secondVar:
    maximim = firstVar
else:
    maximum = secondVar
if thirdVar > maximum:
    maximum = thirdVar
print('Максимальное число:', maximum)