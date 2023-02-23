Задание 1:
#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
#  желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#  третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
#  порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time

class TrafficLight():

   
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 4

   
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.__color = color
        print(f'\nСоздан новый объект TrafficLight со стартовым цветом {self.__color}')

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color = ''):

        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_wait)
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        else:
            self.switch_light('зеленый', self.green_color_wait)

        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

tl1 = TrafficLight('красный')
tl1.running('желтый')

Задание 2:
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():

    # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см
    # Определяю его как private из соображений, что это константа, не подлежащая изменению
    __weight = 0.5

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Создан новый объект класса Road длиной {self._length} метров и шириной {self._width} метров')

    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight
        print(f'Вес асфальта, требуемый для укладки полотна толщиной {thickness} см, равен {ret_val} т')

        return ret_val

r1 = Road(100, 5)
w1 = r1.get_weight(10)

r2 = Road(1000, 20)
w2 = r2.get_weight(20)

print(f'Суммарный вес асфальта для двух объектов = {w1 + w2}')

Задание 2:
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"profit": profit, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_full_profit).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

# Solution:


class Worker:

    def __init__ (self, name ='Petr', surname ='Vasechkin', position ='singer', wage= 100, bonus = 20):
        self.name = name
        self.surname = surname
        self.position  = position
        self._income = {'wage': wage, 'bonus': bonus}


class  (Worker):

    def get_full_name(self):
        return self.name  + ' ' + self.surname

    def get_full_salary(self):
        return ._income['wage'] + self._income['bonus']


v_pet = Position ('Vasilii', 'Petechkin', 'dancer', 110, 30)
print(f'New attributes are: )
print (f'Total salary of  {v_pet.get_full_name()} is  {v_pet.get_full_salary()}')

Задание 4
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг — реализовать
перегрузку метода str() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д. """


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    '''2 варианта реализации __str__'''

    # def __str__(self):
    #     return '\n'.join(map(str, self.my_list))

    # def __str__(self):
    #     return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))

Задание 5 Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
    Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
    Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
    скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
    очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
    Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
    При этом работа скрипта не должна завершаться."""

import traceback


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


class CheckAndAdd:

    def __init__(self):
        self.__result = []
        while True:
            data = input('Число: ')
            try:
                self.__result.append(int(data))
            except ValueError as e:
                if data == 'stop':
                    break
                print('Ошибка с моим обработчиком:\n', traceback.format_exc())
            except Exception as e:
                if data == 'stop':
                    break
                raise MyException('Какая-то другая ошибка')

    def __str__(self):
        return ', '.join(map(str, self.__result))


if __name__ == '__main__':
    c = CheckAndAdd()
    print(c)
    d = CheckAndAdd()
    print(d)
