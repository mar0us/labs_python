from math import fabs

def task1():
    s = input("введите строку: ")
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:len(s)-2])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))

# task1()

def task2():
    s = input("введите строку: ")
    part1 = s[(len(s) + 1) // 2:]
    part2 = s[:(len(s) +1) //2]
    print(part1 + part2)

# task2()

def task3():
    s = input("введите строку: ")
    print(
            s[:s.find("h")+1] +
            s[s.rfind("h")-1: s.find("h"): -1] +
            s[s.rfind("h"):]
        )

# task3()

def task4():
    s = input("введите строку: ")
    index = s.find("f") if s.rfind("f") == s.find("f") else str(s.find("f")) + str(s.rfind("f"))
    print(index if index != -1 else "")

# task4()

def task5():
    l = [5, 2, 3, 4, 5, 6]
    res = [l[i] for i in range(1, len(l)) if l[i] > l[i-1]]
    print(" ".join([str(el) for el in res]))


task5()

def task6():
    l = [-1, 2, -3, -5, -5, 6]
    for i in range(1, len(l)):
        if l[i]/fabs(l[i]) == l[i-1]/fabs(l[i-1]):
            print(f"пара: {l[i-1]} {l[i]}")
            break

# task6()

def task7():
    l = [5, 2, 3, 4, 5, 6, 1]
    # res = [l[::2], l[1::2]]
    res = []
    for i in range(0, len(l), 2):
        if i+1 >= len(l):
            res.append(l[i])
            break
        res.append(l[i+1])
        res.append(l[i])
    print(" ".join([str(el) for el in res]))

# task7()

def task8():
    l = [5, 2, 3, 4, 5, 6, 1]
    res = [el for el in l if l.count(el) == 1]
    print(res)

# task8()