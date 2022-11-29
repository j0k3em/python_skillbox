text = input("Сообщение: ").split()

def back_text(list):
    spec_sym = "!,@,#,$,%,^,;,№,:,&,?,*,(,),-,=,+,[,],{,},?,/,.,>,<,\,|,~".split(",")
    spec_sym.append(",")
    new_line = []

    for element in list:
        start = ""
        start_index = - 1
        for spec in spec_sym:
            for sym in element:
                if spec == sym:
                    start_index = element.index(spec)
                    start += spec

        if start_index == 0:
            new_line.append(start[::-1] + element[start_index:0:-1])
        elif start_index > 0:
            new_line.append(element[start_index - 1::-1] + start + element[len(element):start_index:-1])
        elif start_index < 0:
            new_line.append(element[::-1])

    return " ".join(new_line)

new_text = back_text(text)
print("Новое сообщение: ", new_text)