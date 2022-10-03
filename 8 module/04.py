a = int(input())
b = int(input())
c = int(input())
middle = 0
count = 0
for number in range(a, b + 1):
	if number % c == 0:
		count += 1
		middle += number
print('Среднее арифметическое: ', middle / count)