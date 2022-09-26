yoursCube = int(input('Кубик Кости: '))
ownersCube = int(input('Кубик владельца: '))
sum = yoursCube + ownersCube
difference = yoursCube - ownersCube
if yoursCube >= ownersCube:
    print(difference)
    print('Костя платит')
else:
    print(sum)
    print('Владелец платит')
print('Игра окончена')
