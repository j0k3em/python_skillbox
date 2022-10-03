firstInt = int(input('Введите первое число: '))
secondInt = int(input('Введите второе число: '))
thirdInt = int(input('Введите третье число: '))
if firstInt == secondInt == thirdInt:
    print(3)
elif firstInt == secondInt or secondInt == thirdInt or firstInt == thirdInt:
    print(2)
else:
    print(0)
