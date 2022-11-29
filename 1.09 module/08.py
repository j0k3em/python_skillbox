symbols_count = int(input('Введите длину колонтитул: '))
mark_count = int(input('Введите кол-во восклицательных знаков: '))
print('~' * ((symbols_count - mark_count) // 2 + (symbols_count - mark_count) % 2) + '!' * mark_count + '~' * ((symbols_count - mark_count) // 2))