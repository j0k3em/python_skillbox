phrase = input('Введите строку: ')
sCounter = 0
sCounterMax = 0

for symbol in phrase:
  if symbol == 's':
    sCounter += 1
    if sCounter > sCounterMax:
        sCounterMax = sCounter
  else:
    sCounter = 0

print('Самая длинная последовательность:', sCounterMax)