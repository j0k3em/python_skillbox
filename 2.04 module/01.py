def is_vowel(symbol):
    vowel_list = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е", "А", "У", "О", "Ы", "И", "Э", "Я", "Ю", "Ё", "Е"]
    for i_sym in vowel_list:
        if i_sym == symbol:
            return True
    else:
        return False

text = input("Введите текст: ")
text_list = list(text)
vowel_list_in_text = [l for l in text_list if is_vowel(l)]

print()
print("Список гласных букв:", vowel_list_in_text)
print("Длина списка:", len(vowel_list_in_text))