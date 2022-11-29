import random
number_max = int(input("Введите максимальное число: "))
answer = str(random.randint(1, number_max))

print(answer, "Правильный ответ")

number_right = set()
set_answer = set()
set_no = set()
count = 0

while set_answer != {'помогите!'}:
    set_answer = set(input("Нужное число есть среди вот этих чисел: ").split())

    if set_answer == {'помогите!'}:
        if count == 0:
            number_right = {str(i) for i in range(1, number_max + 1)}
        print("Артём мог загадать следующие числа: ", end="")
        for answer in sorted(number_right.difference(set_no)):
            print(answer, end=" ")
        break

    if answer in set_answer:
        if len(set_answer) == 1:
            print(f"Вы угадали это число {answer}")
            break
        count += 1
        number_right.update(set_answer)
        print("Ответ Артёма: Да")

    else:
        set_no.update(set_answer)
        print("Ответ Артёма: нет")