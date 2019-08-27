# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of.txt"

def getFileData(fname):
    with open(fname + '.txt', encoding='UTF-8') as file:
        return [x.split() for x in file]


def setSalary(user, hours):
    norma = int(user[4])
    salary = int(user[2])
    salary_hour = salary / norma

    data = []
    zp = 0
    # data.extend(['Работник', 'ЗП/Н.ч', 'Отраболат', 'Выдать на руки'])
    for itm in hours:

        if itm[0] == user[0] and itm[1] == user[1]:
            user = itm[0] + ' ' + itm[1]
            otrabotal = int(itm[2])

            if otrabotal > norma:
                salary_n = round(salary + (otrabotal - norma) * salary_hour, 1)
                data.extend([user, str(salary) + '/' + str(norma), otrabotal, salary_n])
                zp = zp + salary
            elif otrabotal < norma:
                salary_n = round(salary - (norma - otrabotal) * salary_hour, 1)
                data.extend([user, str(salary) + '/' + str(norma), otrabotal, salary_n])
                zp = zp + salary
            else:
                data.extend([user, str(salary) + '/' + str(norma), otrabotal, salary])
                zp = zp + salary
        # pass
    return data


workers = getFileData('workers')

hours_of = getFileData('hours_of')

for k, itm in list(enumerate(workers)):
    if k == 0:
        continue
    data = setSalary(itm, hours_of)
    # TODO: Реализовать через f"string
    print('Сотрудник: %(worker)s; ЗП/Н.ч : %(salary_hour)s (руб); Отработал: %(worked)d часов; Выдать на руки: %(salary)d руб.' % {
        "worker": data[0], "salary_hour": data[1], "worked": data[2], "salary": data[3]})
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:

def search_ftuits(alpha=all):
    def __rw(_s, content):
        item = []
        item = [x.strip() for x in content if _s in x if x != []]
        if item != []:
            with open(_s + ".txt", "w", newline='\n') as file:
                print("\n".join(map(str, item)), file = file)

    with open('fruits.txt', encoding='UTF-8') as file:
        content = [x.strip() for x in file]

    symbol = list(map(chr, range(ord('А'), ord('Я') + 1)))
    [__rw(itm, content) for itm in symbol]

search_ftuits()
