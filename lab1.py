def task1():
    a = input("введите название фильма: ")
    b = input("введите название кинотеатра: ")
    c = input("введите время: ")

    print(f'Билет на "{a}" в "{b}" на {c} забронирован')

# task1()

def task2():
    a = input("введите строку: ").lower()
    b = input("введите строку: ").lower()
    
    if a != "да" and a != "нет":
        print("НЕВЕРНО")
    elif b != "нет" and b != "да":
        print("НЕВЕРНО")
    else:
        print("ВЕРНО")
    
# for _ in range(4):
#     task2()

def task3():
    login = input("введите логин: ")
    email = input("введите резервный адрес: ")

    # if a.find("@") == -1:
    #     print("логин верный")
    # else:
    #     print("логин неверный")
    # if b.find("@") != -1:
    #     print("резервный адрес верный")
    # else:
    #     print("резервный адрес неверный")


    if not "@" in login:
        print("логин верный")
    else:
        print("логин неверный")
    if "@" in email:
        print("резервный адрес верный")
    else:
        print("резервный адрес неверный")

# for _ in range(3):
#     task3()

def task4():
    print(input())

# task4()

def task5():
    if input("введите строку: "):
        print("НЕТ")
    else:
        print("ДА")

# for _ in range(2):
#     task5()

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

# for _ in range(3):
#     task6()

def task7():
# def task7(num):

    def calc(first_num, second_num, third_num, last_num, mult):
        res = 0
        if first_num <= second_num and first_num <= third_num and first_num <= last_num:
            res = first_num * mult
            first_num = 99
        elif second_num != 10 and second_num <= first_num and second_num <= third_num and second_num <= last_num:
            res = second_num * mult
            second_num = 99
        elif third_num != 10 and third_num <= first_num and third_num <= second_num and third_num <= last_num:
            res = third_num * mult
            third_num = 99
        elif last_num != 10 and last_num <= first_num and last_num <= second_num and last_num <= third_num:
            res = last_num * mult
            last_num = 99
        
        return res, first_num, second_num, third_num, last_num

    num = int(input("введите четырехзначное число: "))
    first_num = num // 1000
    second_num = (num // 100) % 10
    third_num = (num // 10) % 10
    last_num = num % 10

    first_num = first_num if first_num != 0 else 10
    second_num = second_num if second_num != 0 else 10
    third_num = third_num if third_num != 0 else 10
    last_num = last_num if last_num != 0 else 10

    number = 0
    print("введенное число: " + str(num))

    
    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 1000)
    number += res

    first_num = 0 if first_num == 10 else first_num
    second_num = 0 if second_num == 10 else second_num
    third_num = 0 if third_num == 10 else third_num
    last_num = 0 if last_num == 10 else last_num

    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 100)
    number += res
    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 10)
    number += res
    res, first_num, second_num, third_num, last_num = calc(first_num, second_num, third_num, last_num, 1)
    number += res

    print(number)


# nums = [
#     1234,
#     1243,
#     1423,
#     1432,
#     4123,
#     4132,
#     4312,
#     3412,
#     3421,
#     3241,
#     3214,
#     3241,
#     3421,
#     4321,
#     4012,
#     4201,
#     4420,
#     5002,
#     5200,
#     5020,
#     5050
# ]
# for i in range(len(nums)):
#     task7(nums[i])

# task7()

def task8():
    Max = 0
    Min = 999
    count = 0
    while True:
        l = input("введите рост космонавта: ")
        if l == "!":
            break

        l = int(l)
        count = count + 1 if l < 190 and l > 150 else count
        Max = l if l > Max else Max
        Min = l if l < Min else Min

    print(f"подходит: {count} претендента(ов), максимальный рост: {Max}, минимальный {Min}") 


# task8()


def task9():
    while True:
        first_pass = input("введите пароль: ")
        second_pass = input("введите пароль повторно: ")
        if len(first_pass) < 8:
            print("Короткий!")
        elif first_pass.find("123") != -1:
            print("Простой!")
        elif first_pass != second_pass:
            print("Различаются!")
        else:
            print("OK")
            break

# task9()

import numexpr as ne
def task10():
    print("запишите выражение пример 2 + 2")
    while True:
        expression = input().strip()
        if expression.find("x") != -1:
            num = expression.split("x")[0]
            print(num)
            break
        elif expression.startswith("!"):
            expression = int(expression[1:])
            if expression < 0:
                continue
            factorial = 1
            while expression > 1:
                factorial *= expression
                expression -= 1
            print(f"ответ: {factorial}")
            continue

        # да, как бы можно проверять действие как с факториалом и писать еще пару десятков строк кода, а можно воспользоваться сторонним модулем и сделать в 1 строчку
        answer = ne.evaluate(expression)
        print(f"ответ: {answer}")

# task10()

def task11():
    l = int(input("введите высоту пирамиды: "))
    for i in range(1, l+1):
        l -=1
        print(l * " " + (i*2-1) * "*" + l * " ")

# task11()
        
def task12():
    l = int(input("введите число: "))
    run = True
    num = 0
    last_count = 0
    while run:
        for _ in range(last_count+1):
            num += 1
            print(f"{num} ", end="")
            if num >= l:
                run = False
                break

        last_count += 1
        print()

# task12()
        

def task13():
    size = input("введите стороны(ширина x высота) прямоугольника через пробел\n")
    symbol = input("введите символ для рисования: ")
    size = size.split(" ")
    x, y = int(size[0]), int(size[1])

    for i in range(y):
        if i == 0 or i == y - 1:
            print(symbol * x)
            continue
        
        print(symbol + " " * (x-2) + symbol)

# task13()