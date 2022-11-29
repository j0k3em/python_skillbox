text = input("Введите строку с двумя h: ")
text_list = list(text)
start = 0
finish = 2

for start_h in text:
    if start_h == "h":
        break
    start += 1

for finish_h in range(len(text_list) - 1, 0, -1):
    if text_list[finish_h] != "h":
        finish += 1
    else:
        break

finish = len(text_list) - finish
print(text[finish:start:-1])