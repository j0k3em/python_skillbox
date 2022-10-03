reverse_timer = int(input())
for time in range(reverse_timer, -1, -1):
	if time == 0:
		print('Ваша еда готова, осторожно горячo!')
		break
	answer = int(input('Выключить?'))
	if answer == 1:
		print('Ваша еда готова, можете забрать')
		print(time)
		break