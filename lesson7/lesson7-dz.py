from abc import ABC, abstractmethod
from itertools import zip_longest

"""
1. Реализовать класс Matrix (матрица). 
Обеспечить перегрузку конструктора класса (метод init()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() 
для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — п
ервый элемент первой строки первой матрицы складываем 
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for i in self.matrix:
            for j in i:
                result += str(j) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        new_matrix = []
        for (row1, row2) in zip_longest(self.matrix, other.matrix, fillvalue=[]):
            row = []
            for (el1, el2) in zip_longest(row1, row2, fillvalue=0):
                row.append(el1 + el2)
            new_matrix.append(row)
        return Matrix(new_matrix)


# mat = Matrix([[1, 2, 3], [3, 2]])
# print(mat + Matrix([[1, 5, 3], [3, 4], [5, 6]]))


"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: 
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора @property.
"""


class Clothes(ABC):
    name: str

    @abstractmethod
    def calculate_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def calculate_cloth(self):
        return self.size / 6.5 + 0.5


class Suite(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def calculate_cloth(self):
        return 2 * self.height + 0.3


"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. 
Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()). 
Данные методы должны применяться только к клеткам и выполнять 
увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        self.__check_instance(other)
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        self.__check_instance(other)
        result = self.nucleus - other.nucleus
        if result >= 0:
            return Cell(result)
        else:
            print('отрицательное кол-во ячеек')

    def __mul__(self, other):
        self.__check_instance(other)
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        self.__check_instance(other)
        if other.nucleus == 0:
            raise RuntimeError
        return Cell(round(self.nucleus / other.nucleus))

    def __str__(self):
        return f'nucleus: {self.nucleus}'

    @staticmethod
    def make_order(cell, row_size):
        result = ''
        for i in range(1, cell.nucleus + 1):
            result += '*'
            if i % row_size == 0:
                result += '\n'
        return result

    @staticmethod
    def __check_instance(other):
        if not isinstance(other, Cell):
            raise RuntimeError


cell = Cell(8)
cell2 = Cell(4)
print(cell + cell2)
print(cell - cell2)
print(cell * cell2)
print(cell / cell2)

print(Cell.make_order(Cell(10), 3))
