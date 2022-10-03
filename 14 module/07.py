a = int(input())
b = int(input())
while a < b + 1:
    for i in range(10):
        if 3 == str(a).count(str(i)):
            print(a)
    a += 1