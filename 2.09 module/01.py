num_file = open(r'C:\Users\dimal\OneDrive\Рабочий стол\практики\2.09 module\01.txt', encoding='utf-8')
num = [int(i) for i in num_file.read().split()]
num_file.close()
sum_file = open("answer.txt", "w")
sum_file.write(str(sum(num)))
sum_file.close()