while True:
    count_num = 0
    count_upper = 0
    password = input("Придумайте пароль: ")

    for num in password:
        if num.isdigit():
            count_num += 1

    for num in password:
        if num.isupper():
            count_upper += 1

    if password.isalnum() and count_num >= 3 \
            and len(password) >= 8 and count_upper >= 1:
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный! Попробуйте ещё раз.")