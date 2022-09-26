yourPlace = int(input('Введите место в списке поступающих: '))
yourScores = int(input('Введите количество баллов за экзамен: '))
if yourPlace <= 10 and yourScores >= 290:
    print('Поздравляем, вы поступили!')
    print('Бонусом вам будет начисляться стипендия.')
elif yourPlace <= 10 and yourScores < 290:
    print('Поздравляем, вы поступили!')
    print('Но вам не хватило баллов для стипендии.')
else:
    print('К сожалению, вы не поступили.')
