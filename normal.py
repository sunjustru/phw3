import math


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    F1 = F2 = i = 1
    F = []
    while i <= m:
        if i == 1:
            F3 = 1
        else:
            F3 = F1 + F2

        F1 = F2
        F2 = F3

        F.append(F3)
        i +=1

m = int(input("Введите M элиментов"))
print(fibonacci(1, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort_list = []

    while origin_list:
        min_num = min(origin_list)
        sort_list.append(min_num)
        origin_list.pop(origin_list.index(min_num))
    # pass
    return sort_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

mixed = [0, 2, 3, 4, 5, 6, 1, 0, -23, 32]
filter_fn = [item for item in mixed if item > 5]

print(filter_fn)


# Не правильно понял задание что необходимо сделать;
# def filter_fn(data_list, order='ASC'):
#     '''
#     Функция фильтрации;
#     :param data_list: Принимает список данных из чисел и букв
#     :param order:Фильтрация: DESC — от максимума до минимума; ASC — дефолт от минимума до максимума
#     :return:
#     '''
#
#     def filter_list(f_list):
#         t_res = []
#         while f_list:
#             if order == 'DESC':
#                 t_order = max(f_list)
#             else:
#                 t_order = min(f_list)
#             t_res.append(t_order)
#             f_list.pop(f_list.index(t_order))
#         return t_res
#
#
#     # Формируем список числовой
#     num = [x for x in data_list if (type(x) == float) | (type(x) == int)]
#     # Формируем список буквенный
#     abc = [x for x in data_list if (type(x) == str)]
#
#     if num:
#         num = filter_list(num)
#     if abc:
#         abc = filter_list(abc)
#
#     return num + abc

#print(filter_fn([2, 10, -12, 2.5, 20, -11, 4, 4, 0,'dsd','3232ds','fdfdf']))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

#Противоположные стороны параллелограмма имеют одинаковую длину:
def _paral(a, b, c, d):
    # вычесляем длинну сторон
    def length(A1, A2):
        return math.sqrt((A1[0] - A2[0]) ** 2 + (A1[1] - A2[1]) ** 2)

    AB = length(a, b)
    CD = length(c, d)
    BC = length(b, c)
    AD = length(a, d)

    if AB == CD and BC == AD:
        return True
    else:
        return False


print(_paral((-2.3, 4), (8.5, 0.7), (5, 10), (3, 7)))
