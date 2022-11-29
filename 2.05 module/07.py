while True:
    ip_adress = input("Введите IP: ").split(".")
    for sym in ip_adress:
        if len(ip_adress) != 4:
            print("Адрес - это четыре числа, разделенные точками")
            break
        elif not sym.isdigit():
            print(f"{sym} не целое число")
            break
        elif not (0 <= int(sym) <= 255):
            print(f"Число {sym} не подходит критериям от 0 до 256")
            break
    else:
        print("IP-адрес корректен")
        break