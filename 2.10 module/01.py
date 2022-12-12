with open('people.txt', encoding='UTF-8') as people_file:
    try:
        people_file = people_file.readlines()
        count = sum([len(people.strip()) for people in people_file])
        for string, i_line in enumerate(people_file, 1):
            if len(i_line.strip()) < 3:
                raise BaseException(f'Длина {string} строки меньше 3 символов')
    except BaseException as message:
        print(message)
    finally:
        print('Общее количество символов:', count)
