print('Начался рабочий день.')
tasks = 0
call = False
i = 0
while i < 8:
	print('Начался ', i + 1, '-й час')
	print('Сколько задач решит Максим?')
	task = int(input())
	tasks += task
	print('Звонит жена. Взять трубку? (1 — да, 0 — нет):')
	wife_call = int(input())
	if wife_call == 1:
		call = True
	i += 1
print('Рабочий день закончился. Всего выполнено задач:', tasks)
if (call == True):
	print('Нужно зайти в магазин')