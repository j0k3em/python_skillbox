word = input("Введите слово: ")
letters = list(word)
count_of_letters = len(letters)
diff_sym = 0
count = 0
for i in range(count_of_letters):
    count = 0
    for sym in letters:
        if letters[i] == sym:
           count += 1
    if count >= 2:
        diff_sym += 1

result = len(letters) - diff_sym
print("Кол-во уникальных букв: ", result)