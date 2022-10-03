rows = int(input('Введите количество рядов: '))
seats = int(input('Введите количество сидений: '))
meters = int(input('Введите количество метров между рядами: '))
row = '\n' + '=' * seats + ' ' + '*' * meters + ' ' + '=' * seats 
print(row * rows + '\n') 