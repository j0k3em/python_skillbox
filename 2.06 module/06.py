count_words = int(input("Введите количество пар слов: "))
text_dict = dict()

for i_count in range(1, count_words + 1):
    print(f"{i_count} пара: ", end = "")
    text = input().split(" - ")
    text_dict[text[0]] = text[1]

while True:
    word = input("Введите слово: ")
    for i_word in text_dict:
        if i_word == word:
            print("Синоним:", text_dict[i_word])
            break
        elif word == text_dict[i_word]:
            print("Синоним:", i_word)
            break
    else:
        print("Такого слова в словаре нет.")