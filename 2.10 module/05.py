result = []
with open('calc.txt', encoding='utf-8') as calculator:
    for line in calculator.readlines():
        try:
            result.append(eval(line))
        except:
            if input('Обнаружена ошибка:' + line + 'Хотите исправить?') == 'да':
                line = input('Введите исправленную строку:')
                result.append(eval(line))
print(sum(result))
