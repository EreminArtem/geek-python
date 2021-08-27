"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import random
from functools import reduce
from itertools import count, cycle


def salary():
    from sys import argv
    sn, hours, salary = argv
    print(int(hours) * int(salary))


# salary()

"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. 
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def work_2():
    result = []
    prev = 0
    for i in [random.randint(1, 1000) for i in range(1, 15)]:
        if prev < i:
            result.append(i)
        prev = i

    print(result)


# work_2()

"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""


def work_3():
    return [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]


# print(work_3())


# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

def unic_number():
    numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    return [i for i in numbers if numbers.count(i) == 1]


# print(unic_number())


"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


def multiply_list():
    numbers = [i for i in range(100, 1000)]
    return reduce(lambda acc, num: acc * num, numbers)


# print(multiply_list())

"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. 
    Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
    Необходимо предусмотреть условие его завершения.
"""


def nums_generator(start):
    for i in count(start):
        if i > 100:
            break
        print(i)


def repeat_list():
    list_num = [1, 2, 3]
    counter = 0
    for i in cycle(list):
        if counter > 100:
            break
        print(i)
        counter += 1


# nums_generator(10)
# repeat_list()


"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 
Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, 
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. 
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


def fact(n):
    factorial = 1

    for i in range(2, n + 1):
        factorial *= i
        yield factorial


# for i in fact(4):
#     print(i)