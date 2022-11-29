text = 'О Дивный Новый мир!'

def crypto(input_user):
    return [value for index, value in enumerate(input_user) if is_prime(index)]

def is_prime(number):
    for i_num in range(2, number):
        if number % i_num == 0:
            print(i_num)
            return False
    return True

result = crypto(text)
print(result)
