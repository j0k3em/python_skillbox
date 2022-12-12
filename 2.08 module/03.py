def fibonacci(n, list_fib):
  if len(list_fib) != n:
    list_fib.append(sum(list_fib[len(list_fib)-2:len(list_fib)]))
    fibonacci(n, list_fib)

n = int(input("Введите позицию числа в ряде Фибоначчи: "))
list_fib = [1]
fibonacci(n, list_fib)
print("Число:", list_fib[n - 1])