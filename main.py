# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task1():
    print("Задание 1.")
    my_list = [0, "один", True, "переднее клыло", [1, 2, 3, 4]]
    types = [int, str, bool, list]
    means = ["Целое число", "Строка", "Булево", "Список"]
    for element in my_list:
        i = types.index(type(element))
        print(f"Элемент списка my_list: {element}, под номером {i}, имеет тип: {means[i]}")


def task2():
    print("Задание 2.")
    my_list = []
    while True:
        element = input("Введите следующий элемент списка, просто Enter - конец: ")
        if element == "":
            break
        my_list.append(element)
    for i in range(1, len(my_list), 2):
        my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
    for i in range(0, len(my_list)):
        print(my_list[i])


# Задание 3. Решение через List
def task_by_list3():
    months = ["Январь",
              "Февраль",
              "Март",
              "Апрель",
              "Май",
              "Июнь",
              "Июль",
              "Август",
              "Сентябрь",
              "Октябрь",
              "Ноябрь",
              "Декабрь"]
    print(months[int(input("Введите номер месяца (1..12): ")) - 1])


def task_by_dict3():
    months = {1: "Январь",
              2: "Февраль",
              3: "Март",
              4: "Апрель",
              5: "Май",
              6: "Июнь",
              7: "Июль",
              8: "Август",
              9: "Сентябрь",
              10: "Октябрь",
              11: "Ноябрь",
              12: "Декабрь"}
    print(months[int(input("Введите номер месяца (1..12): "))])


def task4():
    s = input("Введите предложение: ")
    l = s.split()
    for word in l:
        print(f"{l.index(word)} - {word[0:9]}")


def task5():
    rating1 = [7, 5, 3, 3, 2]
    while True:
        n = input("Введите число (Enter - выход): ")
        if n == "":
            break
        rating = rating1[:]
        m = int(n)
        rating.insert(0, m)
        rating.sort(reverse=True)
        print(rating)


def task6():
    a = (0, [1, 2, 3, 4, 5, 6])
    print(a[1])
    t_list = list()
    while True:
        n = input("Введите номер товара (ENTER - конец): ")
        if n == "":
            break
        t_dict = dict()
        while True:
            product_key = input("Введите название (ENTER - конец: ")
            if product_key == "":
                break
            product_value = input("Введите значение: ")
            t_dict[product_key] = product_value
        t_tuple = (n, t_dict)
        t_list.append(t_tuple)
    '''
    print(t_list)
    t_list = [
        (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
        (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
        ]

    '''
    out_dict = dict()
    for l in t_list:
        t_dict = l[1]
        for k, v in t_dict.items():
            if k not in out_dict.keys():
                out_dict[k] = list()
            if v not in out_dict[k]:
                out_dict[k].append(v)
    print(f"Введено: {t_list}")
    print(f"Получено: {out_dict}")


if __name__ == '__main__':
    task1()
    task2()
    task_by_list3()
    task_by_dict3()
    task4()
    task5()
    task6()
