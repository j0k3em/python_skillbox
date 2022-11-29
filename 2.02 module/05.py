films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favourite_films = []
user_intresting = ""
while user_intresting != "end":
    user_intresting = input("Введите название фильма для завершения введите end: ")
    if user_intresting in films:
        favourite_films.append(user_intresting)
    elif user_intresting == "end":
        break
    else:
        print("Такого фильма нет, или вы ввели с маленькой буквы")
print("Список любимых фильмов: ", favourite_films)