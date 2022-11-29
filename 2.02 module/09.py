word = input("Введите слово: ")
symbols = list(word)
count_of_word = len(symbols) - 1
new_word = []
for index in range(count_of_word, -1, -1):
    new_word.append(symbols[index])
if new_word == symbols:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")