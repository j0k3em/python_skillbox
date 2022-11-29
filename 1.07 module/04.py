violations = 0
for sector in range(30, 36):
    count = int(input('Людей в секторе: '))
    if count > 10:
        print('Нарушение! Слишком много людей в секторе!')
        violations += 1
    else:
        print('Всё спокойно.')
print('Количество нарушений =', violations)
