def histogramma(text):
    text_dict = dict()
    for sym in text:
        if sym in text_dict:
            text_dict[sym] += 1
        else:
            text_dict[sym] = 1
    return text_dict

text_input = input("Введите текст: ")
result = histogramma(text_input)
print(result, "result")
for i_result in sorted(result):
    print("{0} : {1}".format(i_result, result[i_result]))
    
print()
print("Инвертированный словарь частот:")
for i in range(max(result.values())):
    list = []
    for i_list in result:
        if result[i_list] == i + 1:
            list.append(i_list)
    print(f"{i + 1} : {list}")