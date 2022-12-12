import random
with open('out-file.txt', 'w') as output:
    summary = 0
    try:
        while summary < 777:
            number = input('Введите число: ')
            if random.randint(1, 13) == 1:
                raise BaseException
            output.write(number + '\n')
            summary += int(number)
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except BaseException:
        print('Вас постигла неудача!')
    finally:
        output.close()
        with open('out-file.txt', 'r') as out_read:
            print('Содержимое файла out_file.txt: ')
            print(out_read.read())