def score_key(tuple):
    return tuple[1][0] - tuple[1][1]

score_tuple = tuple()
score_table = dict()
how_many = int(input("Сколько записей вносится в протокол? "))
print("Записи (результат и имя):\n")

for queue in range(how_many):
    score, name = input('{} запись: '.format(queue+1)).split()
    score = int(score)
    if name in score_table:
        if score > score_table[name][0]:
            score_table[name] = (score, queue)
    else:
        score_table[name] = (score, queue)

score_tuple = tuple(score_table.items())
res_list = sorted(score_tuple, key=score_key, reverse=True)
winner = 1

print("Итоги соревнований:")
for i_winner in res_list[0:3]:
    name = i_winner[0]
    score = i_winner[1][0]
    print(f"{winner} место. {name} ({score})")
    winner += 1