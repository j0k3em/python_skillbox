firstSubject = int(input('Введите количество баллов по русскому языку: '))
secondSubject = int(input('Введите количество баллов по математике: '))
thirdSubject = int(input('Введите количество баллов по информатике: '))
if firstSubject + secondSubject + thirdSubject >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')
