def reverse(num):
  return int(''.join(reversed(list(str(num)))))
 
N = int(input('Введите первое число: '))
K = int(input('Введите второе число: '))
 
first_revers = reverse(N)
second_revers = reverse(K)
 
print('\nПервое число наоборот:', first_revers)
print('Второе число наоборот:', second_revers)
print('\nСумма:', N + K)
print('Сумма наоборот:', first_revers + second_revers)
