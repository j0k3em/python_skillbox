import random

def rock_paper_scissors():
    var = ['ножницы', 'камень', 'бумага']
    answer = input('Камень, ножницы или бумага? ')
    choise = random.choice(var)
    print('Выбор компьютера:', choise)
    if answer.lower() == choise:
        print('Ничья')
        return 0
    if answer.lower() == 'камень':
        if choise == 'бумага':
            print('Вы проиграли')
        else:
            print('Вы победили')
    if answer.lower() == 'ножницы':
        if choise == 'камень':
            print('Вы проиграли')
        else:
            print('Вы победили')
    if answer.lower() == 'бумага':
        if choise == 'ножницы':
            print('Вы проиграли')
        else:
            print('Вы победили')

def guess_the_number():
    guesses_made = 0
    number = random.randint(1, 10)
    while True:
        guess = int(input('Введи число: '))
        guesses_made += 1
        if guess < number:
            print('Твое число меньше.')
        if guess > number:
            print('Твое число больше.')
        if guess == number:
            print('Ты угадал! С', guesses_made, 'попытки')
            break


def mainMenu():
    while True:
        game = int(input('Выберите игру:\n'
                         '1 - Угадай число\n'
                         '2 - Камень, ножницы, бумага\n'
                         '0 -  Выход\n'))
        print()
        if game == 1:
            guess_the_number()
        elif game == 2:
            rock_paper_scissors()
        elif game == 0:
            return
        else:
            print('Неверная команда!')

mainMenu()