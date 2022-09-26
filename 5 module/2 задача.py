firstVar = int(input('Введите первую переменную: '))
secondVar = int(input('Введите вторую переменную: '))
thirdVar = int(input('Введите третью переменную: '))
if firstVar > secondVar and firstVar > thirdVar:
    print('Максимальное число:', firstVar)
elif secondVar > firstVar and secondVar > thirdVar:
    print('Максимальное число:', secondVar)
else:
    print('Максимальное число:', thirdVar)
