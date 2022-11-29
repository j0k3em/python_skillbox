word = input("Введите слово: ")
letters_of_count = list(word)
count_of_word = len(letters_of_count) - 1
new_word = []
for index in range(count_of_word, -1, -1):
    new_word.append(letters_of_count[index])
if new_word == letters_of_count:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")