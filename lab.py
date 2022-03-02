def task1():
    # s = input("введите текст")
    s = "рыба рыба рыба рыба рыба камыш тетрадь жук телефон рыба подушка телефон"
    l = s.split()
    d = {word : s.count(word) for word in l}

    print("исходная строка:\n" + s)
    for word in d:
        print(f"слово {word} встречается {d[word]} раз(а)")

# task1()

# условия задания отличаются от входных данных в примере поэтому становится немного не понятно откуда берутся слова, пусть слова берутся из файла в котором они записаны парами и пользователю потом предлагается ввести слово для поиска его синонима
def task2():
    words1 = {}
    words2 = {}
    with open("words.txt", "r") as f:
        words1 = {word.split()[0]: word.split()[1] for word in f}
        words2 = {words1[key]: key for key in words1}
    
    print("исходные слова:\n" + "\n".join([f"{word} {words1.get(word)}" for word in words1]))
    w = input("введите слово для поиска синонима: ")
    print(f"синонимом к слову {w} является слово {words1.get(w) if words2.get(w) is None else words2.get(w)}")

# task2()

def task3():
    n = int(input("введите количество строк: "))

    condidates = {}
    for i in range(n):
        key, value = input().split()
        condidates.update({key: (int(condidates[key]) + int(value)) if condidates.get(key) is not None else int(value)})
    
    print(f"количество голосов отданных за призедентов:\n" + "\n".join([f"{key} {condidates[key]}" for key in condidates]))

# task3()

def task4():
    n = int(input("введите количество файлов: "))
    rights_list = {"R": [], "W": [], "X": []}
    for _ in range(n):
        f = input().split()
        file_name, rights = f[0], f[1:]
        for el in rights:
            rights_list[el].append(file_name)
    
    answers = []
    m = int(input("введите количество операций над файлами: "))
    for _ in range(m):
        operation, file_name = input().split()
        for el in rights_list:
            if operation[0].lower() == el.lower():
                if rights_list[el].count(file_name) != 0:
                    answers.append("OK")
                else:
                    answers.append("Accept denied")
                break
            else:
                if rights_list["X"].count(file_name) != 0:
                    answers.append("OK")
                else:
                    answers.append("Accept denied")
                break

    print("результаты выполнения команд:\n" + "\n".join(answers))
task4()