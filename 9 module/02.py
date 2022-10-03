pirate_counter = 0
for pirate in range(10):
  phrase = input('Введите фразу: ')
  if phrase == 'Карамба' or phrase == 'карамба':
    pirate_counter +=1
print(pirate_counter, 'пиратов попадут на борт!')