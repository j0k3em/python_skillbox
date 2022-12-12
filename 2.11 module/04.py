import random

class Children:
    def __init__(self, name, age, condition, hangry):
        self.name = name
        self.age = age
        self.condition = condition
        self.hangry = hangry

    def feed(self):
        if self.hangry:
            self.hangry = False
        else:
            self.condition = False

    def calm_down(self):
        self.condition = True

    def print_child(self):
        print(f"\tИмя: {self.name}, возраст: {self.age}, спокойный: {self.condition}, голодный: {self.hangry}".replace("True", "Да").replace("False", "Нет"))

class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def print_short(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Детей: {len(self.children)}")

    def print_info(self):
        print(f"\nИмя: {self.name}, Возраст: {self.age}, Дети:")
        for child in self.children:
            child.print_child()

    def calm_down(self):
        for child in self.children:
            child.calm_down()

    def feed(self):
        for child in self.children:
            child.feed()

    def create_child(self, name):
        self.children.append(Children(name, random.randint(1, self.age - 16),
                                      random.choice([True, False]),
                                      random.choice([True, False])))

def read_file():
    parents = []
    with open("text.txt", encoding = "UTF-8") as file:
        file=file.readlines()
        for line in file:
            line_list = line.split()
            if line_list[0] == "p":
                parents.append(Parent(line_list[1], int(line_list[2])))
            else:
                parents[-1].create_child(line_list[0])
    return parents

def print_parents(parents):
    for parent in parents:
        parent.print_info()

def print_parents_short(parents):
    for id, parent in enumerate(parents):
        print(id + 1, end=") ")
        parent.print_short()

def main_menu(parents):
    while True:
        print_parents_short(parents)
        print("\nВыберите действией:"
              "\nВыберите родителя для действия!"
              "\n0 - Вывести родителей и детей на экран")
        choice = int(input(""))
        if choice == 0:
            print_parents(parents)
        elif 0 < choice <= len(parents):
            deep_menu(parents[choice - 1])
        else:
            print("Некорректная команда!")

def deep_menu(parent):
    print("Выберите действией:"
          "\n1 - Накормить всех детей"
          "\n2 - Успокоить всех детей"
          "\n0 - Вернуться в главное меню")
    choice = int(input())
    if choice == 1:
        parent.feed()
        parent.print_info()
    elif choice == 2:
        parent.calm_down()
        parent.print_info()
    elif choice != 0:
        print("Некорректная команда!")

parents = read_file()
main_menu(parents)