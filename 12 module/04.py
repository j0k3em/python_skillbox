def reverse(num):
    num_reverse = ''
    while num > 0:
        num_reverse += str(num % 10)
        num = num // 10
    print(int(num_reverse))

reverse(int(input("Введите число, которое хотите перевернуть: ")))