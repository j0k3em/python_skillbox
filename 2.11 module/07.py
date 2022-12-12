import random


class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 20
        self.house.use_food()

    def work(self):
        self.satiety -= 20
        self.house.add_salary()

    def get_food(self):
        self.house.add_food()
        self.house.use_money()

    def play(self):
        self.satiety -= 20

    def check_satiety(self):
        if self.satiety < 20:
            return True
        else:
            return False

    def check_all(self):
        if self.house.check_house() and self.satiety >= 0:
            return True
        else:
            return False

    def action(self):
        is_dead = False
        value = random.randint(1, 6)
        if self.check_satiety() and not self.house.check_food():
            self.eat()
        elif self.house.check_food() and not self.house.check_money():
            self.get_food()
        elif self.house.check_money() and not self.check_satiety():
            self.work()
        elif value == 1 and not self.check_satiety():
            self.work()
        elif value == 2 and not self.house.check_food():
            self.eat()
        elif value > 2 and not self.check_satiety():
            self.play()
        else:
            print(self.name, "умер,", end="")
            is_dead = True
        return is_dead


class House:
    def __init__(self):
        self.food = 50
        self.money = 0

    def check_food(self):
        if self.food < 10:
            return True
        else:
            return False

    def check_money(self):
        if self.money < 50:
            return True
        else:
            return False

    def add_salary(self):
        self.money += 50

    def add_food(self):
        self.food += 10

    def use_food(self):
        self.food -= 10

    def use_money(self):
        self.money -= 50

    def check_house(self):
        if self.money >= 0 and self.food >= 0:
            return True
        else:
            return False

house = House()
first_human = Human("Мишаня", house)
second_human = Human("Санёк", house)

days = int(input("Введите кол-во дней: "))
for i in range(1, days + 1):
    if first_human.action() or second_human.action():
        print(f"на {i} день")
        break

    if not first_human.check_all() or not second_human.check_all():
        print(f"Нет ресурсов на {i} день")
        break
else:
    print(f"Прожито {days} дней")