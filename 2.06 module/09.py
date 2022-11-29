number_kin = int(input("Введите количество человек: "))
kin_level = dict()
main_kin_1 = dict()

for i in range(number_kin - 1):
    parent, kin = input(f"{i + 1} пара: ").split()
    main_kin_1[parent] = kin
    kin_level[parent] = 0
    kin_level[kin] = 0
print(main_kin_1)
for i_kin in main_kin_1:
    one_of_parent = i_kin
    print(one_of_parent, "one_of_parent")
    while one_of_parent in main_kin_1:
        one_of_parent = main_kin_1[one_of_parent]
        kin_level[i_kin] += 1
        print(kin_level)

for i_kin in sorted(kin_level):
    print(i_kin, kin_level[i_kin])