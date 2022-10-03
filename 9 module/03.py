text = input('Введите текст сообщения: ')
couter = 0
for symbol in text:
    couter += 1
    if symbol == '*':
        print('Символ ‘*’ стоит на позиции', couter)