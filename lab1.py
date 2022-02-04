def task1():
    a = input("введите название фильма: ")
    b = input("введите название кинотеатра: ")
    c = input("введите время: ")

    print(f'Билет на "{a}" в "{b}" на {c} забронирован')

def task2():
    a = input("введите строку: ")
    b = input("введите строку: ")
    if a == "да" and b == "нет":
        print("ВЕРНО")
    elif a == "нет" and b == "да":
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

def task3():
    a = input("введите логин: ")
    b = input("введите резервный адрес: ")

    if a.find("@") == -1:
        print("логин верный")
    else:
        print("логин неверный")
    if b.find("@") != -1:
        print("резервный адрес верный")
    else:
        print("резервный адрес неверный")

def task4():
    print(input())

def task5():
    if input("введите строку: "):
        print("НЕТ")
    else:
        print("ДА")

def task6():
    a = input("введите число: ")
    max_num = [0, -1]
    min_num = [int(a), -1]
    for i in range(3):
        num = int(a[i])
        if num > max_num[0]:
            max_num = [num, i]
        if num < min_num[0]:
            min_num = [num, i]

    for i in range(3):
        if not i == max_num[1] and not i == min_num[1]:
            third_num = int(a[i])

    if (max_num[0] + min_num[0]) / 2 == third_num:
        print("Вы ввели красивое число")
    else:
        print("Жаль, вы ввели обычное число")

def task7():
    num = int(input("введите четырехзначное число: "))
    first_num = num // 1000
    second_num = (num // 100) % 10
    third_num = (num // 10) % 10
    last_num = num % 10

    # print(f"1: {first_num}, 2: {second_num}, 3: {third_num}, 4: {last_num}")
    min_first = 0
    min_second = 0
    min_third = 0
    min_last = 0

    
task7()
