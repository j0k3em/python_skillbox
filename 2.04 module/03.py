import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners_team = [first_team[l] if first_team[l] > second_team[l]
                else second_team[l] for l in range(20)]

print("Первая команда: ", first_team)
print("Вторая команда: ", second_team)
print("Победители тура: ", winners_team)