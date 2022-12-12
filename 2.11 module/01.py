import random


class Unit:
    def __init__(self, healthpoints):
        self.hp = healthpoints


first = Unit(100)
second = Unit(100)

while first.hp > 0 and second.hp > 0:
    attacker = random.randint(1, 2)
    damage = random.randint(1, 100)
    if attacker == 1:
        second.hp -= damage
        print('Первый юнит аттаковал второго\nЗдоровье второго юнита: {}'.format(second.hp))
    else:
        first.hp -= damage
        print('Второй юнит аттаковал первого\nЗдоровье первого юнита: {}'.format(first.hp))
if first.hp > 0:
    print('Победил первый юнит')
elif second.hp > 0:
    print('Победил второй юнит')
