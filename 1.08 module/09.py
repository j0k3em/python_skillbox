x = int(input())
first = 0
second = 0
for n in range(1, 64, 2):
	first += (x - n)
for n in range(2, 65, 2):
	second += (x - n)
print('res =', first / second)