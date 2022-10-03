word_len = 0
max_len = 0
phrase = input('Введите текст: ')

for symbol in phrase:
  if symbol != ' ':
    word_len += 1
  else:
    word_len = 0
  if word_len > max_len:
    max_len = word_len

print('Самое длинное слово, букв:', max_len)