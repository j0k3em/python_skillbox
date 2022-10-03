N = int(input('Введите число карточек: '))
remains = N - 1
composition = 1
count = 0
for cards in range(1, N + 1):
    composition *= cards
    count += 1
for cards in range(N):
    card = int(input('Введите номер карточки: '))
    composition /= card
    count -= 1
    if count == 1:
        print('Номер пропавшей карточки:', composition)
        break
