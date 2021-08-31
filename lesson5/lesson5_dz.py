"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
import json
import random
import re
import statistics
import string
from functools import reduce


def create_and_write_file():
    try:
        with open("salary.txt", "w") as file:
            is_continue = True
        while is_continue:
            text = input("Введите строку: ")
            if text == '':
                is_continue = False
                continue
            print(f'{text}', file=file)
    except IOError:
        print("Что-то пошло не так")


# create_and_write_file()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def line_counter(file_path):
    try:
        with open(file_path) as file:
            lines = file.readlines()
            print(
                f'Кол-во строк: {len(lines)}',
                [f'{i + 1} строка: {len(v.split())} слов' for i, v in enumerate(lines)]
            )
    except IOError:
        print("Что-то пошло не так")


# line_counter("lesson5/salary.txt")

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""


def salary_helper(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            max_salary = -1
            salaries = dict()
            for line in file.readlines():
                record = line.split()
                salary = float(record[1])
                salaries[record[0]] = salary
                if salary > max_salary:
                    max_salary = salary

            print(f'Заплата меньше 20: {[k for k, v in salaries.items() if v < 20000]}')
            print(f'Средняя зарплата: {round(statistics.mean(salaries.values()), ndigits=2)}')
    except IOError:
        print("Что-то пошло не так")


# salary_helper("lesson5/salary.txt")

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""


def numbers():
    rus_nums = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    try:
        with open('lesson5/numbers.txt', encoding='utf-8') as file:
            with open('new_numbers.txt', 'w', encoding='utf-8') as new_file:
                for line in file.readlines():
                    record = line.split()
                    print(f'{rus_nums[int(record[2])]} {record[1]} {record[2]}', file=new_file)
    except IOError:
        print("Что-то пошло не так")


# numbers()

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def numbers_in_file():
    try:
        with open("random_numbers.txt", "a+") as file:
            for i in range(0, 42):
                file.write(f'{random.randint(0, 1000)} ')
            file.flush()
            file.seek(0)
            summ = reduce(lambda acc, x: acc + x, map(lambda s: int(s), file.readline().split()))
            print(summ)
    except IOError:
        print("Что-то пошло не так")


# numbers_in_file()

"""
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def study():
    try:
        with open('study.txt', encoding='utf-8') as file:
            study_dict = {}
            for line in file.readlines():
                raw = line.split()
                "".strip()
                lesson_name = raw[0][:-1]
                summ = 0
                # f = filter(lambda i: i != '', map(lambda s: ''.join(re.findall('\d+', s)), raw[1:]))
                # study_dict[lesson_name] = reduce(lambda acc, x: int(acc) + int(x), f)
                # так вроде более читаемо
                for i in raw[1:]:
                    w = ''.join(re.findall('\d+', i))
                    if w != '':
                        summ += int(w)
                study_dict[lesson_name] = summ
            print(study_dict)
    except IOError:
        print("Что-то пошло не так")


# study()

"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""


def counter():
    try:
        with(open("firms.txt")) as file:
            firm_count = 0
            total_profit = 0
            firm_dict = {}
            for i in file:
                row = i.split()
                profit = int(row[2]) - int(row[3])
                if profit > 0:
                    total_profit += profit
                    firm_count += 1
                firm_dict[row[0]] = profit
                avg_dict = {'average_profit': round(total_profit / firm_count, 2)}
            with open('firms.json', 'w') as json_file:
                json.dump([firm_dict, avg_dict], json_file)
    except IOError as err:
        print(err)


counter()
