fourDigitNumber = int(input('Введите четырёхзначное число: '))
d = fourDigitNumber % 10
x = fourDigitNumber // 10
c = x % 10
y = x // 10
b = y % 10
z = y // 10
a = z % 10
print(int(str(d) + str(c) + str(b) + str(a)))
