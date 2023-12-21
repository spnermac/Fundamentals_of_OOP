# TODO Написать 3 класса с документацией и аннотацией типов
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
import doctest


class Ellipse:
    def __init__(self, radius_1: int, radius_2: int):

        """"
        Создание и подготовка к работе обьекта 'Эллипс'
        :param radius_1 - большая полуось эллипса
        :param radius_2 - малая полуось эллипса
        Примеры:
        ellipse_1  = Ellipse(16,9)
        """

        if not isinstance(radius_1, int):
            raise TypeError('Длины полуосей должны быть типа int')

        if not isinstance(radius_2, int):
            raise TypeError('Длины полуосей должны быть типа int')

        if radius_1*radius_2 <=0 or radius_1 <= 0:
            raise ValueError('Длины полуосей должны быть положительными')

        self.radius_1 = radius_1
        self.radius_2 = radius_2

        def area_count(self, radius_1: int, radius_2: int) -> int:
            """""
             Расчет площади эллипса:
             radius_1 - большая полуось эллипса
             radius_2 - малая полуось эллипса
             Результат - площадь
             """
            ...

        def eccentricity_count(self, radius_1: int, radius_2: int) -> float:
            """"
             Расчет эксцентриситета эллипса
             radius_1 - большая полуось эллипса
             radius_2 - малая полуось эллипса
             Результат - эксцентриситет
             """
            ...

class Rivers:
    def __init__(self, name: str, length: int, deep: int):

        """"
        Создание и подготовка к работе обьекта 'Реки'
        :param name - Название реки
        :param length - Длина реки
        :param deep - Глубина реки
        Примеры:
        river_1  = Rivers('Нева', 74,9)
        """

        if not isinstance(name, str):
            raise TypeError('Название должно быть типа str')

        if not isinstance(length, int):
            raise TypeError('Длина реки должна быть типа int')

        if length <=0:
            raise ValueError('Длина реки должна быть положительными')

        if not isinstance(deep, int):
            raise TypeError('Глубина реки должна быть типа int')

        if length*deep <=0:
            raise ValueError('Глубина реки должна быть положительными')

        self.name = name
        self.length = length
        self.deep = deep

        def volume_calc(self,length: int, deep: int) -> float:
            """"
             Расчет объёма воды в реке:
             length - длина реки
             deep - глубина реки
             Результат - объем воды в реке
             """
            ...
        def fish_count(self) -> int:
            """"
             Оценка количеста рыбы, которая обитает в реке
             name - название реки
             Результат - количество рыбы в реке
             """
            ...

class Cities:
    def __init__(self,name: str, country: str, people: int):

        """"
       Создание и подготовка к работе обьекта 'Города'
       :param name - Название города
       :param length - Название старны
       :param deep - Население(тыс чел)
       Примеры:
       city_1  = Cities('Москва', 'Россия', 13100)
       """

        if not isinstance(country, str):
            raise TypeError('Страна должна быть типа str')

        if not isinstance(name, str):
            raise TypeError('Название города должно быть типа str')

        if not isinstance(people, int):
            raise TypeError('Количество людей должно быть типа int')

        if people <= 0:
            raise ValueError('Количество людей должно быть положительными')

        self.name = name
        self.country = country
        self.people = people

        def pop_density_count(slef) -> int:
            """"
             Расчет плотности населения города:
             name - город
             people - население
             Результат - плотность населения города
             """
            ...

        def find_continent(self) -> str:
            """"
             Функия по определению континента, на котором распологается город
             country - страна, в которой находится город
             Результат - континент на котором расположен город
             """
            ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
