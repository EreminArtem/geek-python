# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

def check_types():
    stuff = [0, 42, 'noop', True]
    for s in stuff:
        print(type(s))


# check_types()
# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

def swap_elements():
    user_list = []
    print('Вводите элементы списка. Stop чтобы перестать')
    while True:
        answer = input()
        if answer == 'Stop':
            break
        user_list.append(answer)
    i = 0
    while i < len(user_list):
        if i + 1 < len(user_list):
            user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
        i += 2
    print(user_list)


# swap_elements()


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

def seasons_by_list():
    months = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    mouth = int(input('Введите номер месяца: '))
    if mouth > 12 or mouth < 1:
        print('Что-то не так')
    else:
        print(months[mouth - 1])


# seasons_by_list()

def seasons_by_dict():
    months = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
              10: 'Осень', 11: 'Осень', 12: 'Зима'}
    mouth = int(input('Введите номер месяца: '))
    if mouth > 12 or mouth < 1:
        print('Что-то не так')
    else:
        print(months[mouth])


# seasons_by_dict()


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

def split_line():
    line = input('Введите строку: ')
    words = line.split()
    for i, value in enumerate(words):
        if i > 9:
            break
        print(f'{i + 1} {value}')


# split_line()


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

def rang():
    rang = [7, 5, 3, 3, 2]
    rang.sort(reverse=True)

    element = int(input('Введите элемент'))

    for i, value in enumerate(rang):
        if i + 1 < len(rang):
            if value <= element:
                rang.insert(i, element)
                break
            if value > element > rang[i + 1]:
                rang.insert(i + 1, element)
                break
        else:
            rang.insert(i + 1, element)
            break

    print(rang)


# rang()


# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

def store():
    product_list = []
    is_stop = False
    while not is_stop:
        name = input('Введите название товара: ')
        price = float(input('Введите цену товара: '))
        count = int(input('Введите кол-во товара: '))
        unit = input('Введите еденицу измерения: ')
        product_list.append(
            (len(product_list) + 1, {'название': name, 'цена': price, 'количество': count, 'eд': unit})
        )
        is_stop = False if input('Ещё? y/n ') == 'y' else True

    analyzed_products = {'названия': set(), 'цена': [], 'количество': [], 'eд': set()}

    for p in product_list:
        analyzed_products['названия'].add(p[1]['название'])
        analyzed_products['цена'].append(p[1]['цена'])
        analyzed_products['количество'].append(p[1]['количество'])
        analyzed_products['eд'].add(p[1]['eд'])

    print(analyzed_products)

# store()
