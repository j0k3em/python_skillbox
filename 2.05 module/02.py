line = "сейчас я буду писать длинный код на питоне".split()
result = line[0]
print(min(line))
for word in range(len(line)):
    if len(line[word]) > len(result):
        result = line[word]

print(f"Самое длинное слово - {result}, его длина = {len(result)} символов")