zen_file = open(r'02.txt', encoding='utf-8')
reverse_zen = ""
for line in zen_file:
    if not ("\n" in line):
        line = line + "\n"
    reverse_zen = line + reverse_zen
print(reverse_zen)
zen_file.close()