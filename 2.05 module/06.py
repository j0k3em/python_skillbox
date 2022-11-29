s = input("Введите строку: ")
def zip(text):
    result = []
    result.append([text[0]])
    list_count = 0
    # print(len(text))
    for num in range(len(text)):
        for sum in range (num + 1, len(text)):
            if text[num] == text[sum]:
                result[list_count] += text[num]
                break
            else:
                result.append([text[sum]])
                list_count += 1
                break
    return "".join([element[0] + str(len(element)) for element in result])
    print(result)


print("Закодированная строка:", zip(s))