while True:
    ip_adress = input("Введите IP: ").split(".")
    for symbal in ip_adress:
        if len(ip_adress) != 4:
            print("Адрес - это четыре числа, разделенные точками")
            break
        elif not symbal.isdigit():
            print(f"{symbal} не целое число")
            break
        elif not (0 <= int(symbal) <= 255):
            print(f"Число {symbal} не подходит критериям от 0 до 256")
            break
    else:
        print("IP-адрес корректен")
        break