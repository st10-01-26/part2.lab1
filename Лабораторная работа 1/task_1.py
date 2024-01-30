from typing import Union
import doctest

# TODO Написать 3 класса с документацией и аннотацией типов
class Stair:
    """
    Класс описывает модель лестницы
    """
    def __init__(self, number_of_steps: int, height_of_steps: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Лестница"

        :param number_of_steps: Количество ступеней
        :param height_of_steps: Высота ступеней

        Примеры:
        >>> stair = Stair(15, 200)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_steps, int):
            raise TypeError
        if not number_of_steps > 0:
            raise ValueError
        self.number_of_steps = number_of_steps

        if not isinstance(height_of_steps, (int, float)):
            raise TypeError
        if not height_of_steps > 0:
            raise ValueError
        self.height_of_steps = height_of_steps

    def calculating_height_of_stair(self) -> Union[int, float]:
        """
        Функция, которая вычисляет высоту лестницы

        :return: Высота лестницы

        Примеры:
        >>> stair = Stair(15, 200)
        >>> stair.calculating_height_of_stair()
        """
        ...

    def init_width_of_stairway(self, width_of_stair: Union[int, float], number_of_stairways: int) -> Union[int, float]:
        """
        Функция, которая вычисляет ширину лестничного марша

        :param width_of_stair: Ширина всей лестницы
        :param number_of_stairways: Количество лестничых маршей

        :return: Ширина одного лестничного марша

        Примеры:
        >>> stair = Stair(15, 200)
        >>> stair.init_width_of_stairway(2000, 2)
        """
        if not isinstance(width_of_stair, (int, float)):
            raise TypeError
        if not width_of_stair > 0:
            raise ValueError

        if not isinstance(number_of_stairways, int):
            raise TypeError
        if not number_of_stairways > 0:
            raise ValueError
        ...

    def init_type_of_stair(self, number_of_stairways: Union[int, float]) -> str:
        """
        Функция, которая определяет тип лестницы в соответсвтии с количеством лестничных маршей

        :param number_of_stairways: Количество лестничых маршей

        :return: Тип лестницы

        Примеры:
        >>> stair = Stair(15, 200)
        >>> stair.init_type_of_stair(2)
        """
        if not isinstance(number_of_stairways, int):
            raise TypeError
        if not number_of_stairways > 0:
            raise ValueError
        ...

class Window:
    """
    Класс описывает модель окна
    """
    def __init__(self, height: Union[int, float], width: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Окно"

        :param height: Высота окна
        :param width: Ширина окна

        Примеры:
        >>> window = Window(1600, 800)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError
        if not height > 0:
            raise ValueError
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError
        if not width > 0:
            raise ValueError
        self.width = width

    def init_parameters_of_flaps(self, number_of_flaps: Union[int, float]) -> list[list]:
        """
        Функция, которая определяет параметры, дину и ширину, створок в соответствии с количеством створок в окне

        :param number_of_flaps: Количество створок

        :return: Список, содержащий списки, в которых - высота и ширина каждой створки

        Примеры:
        >>> window = Window(1600, 1600)
        >>> window.init_parameters_of_flaps(2)
        """
        if not isinstance(number_of_flaps, int):
            raise TypeError
        if not number_of_flaps > 0:
            raise ValueError
        self.number_of_flaps = number_of_flaps
        ...

    def init_coefficient_of_heat_transfer_resistance(self, type_of_window: str) -> float:
        """
        Функция, которая определяет коэффициент сопротивления теплопередаче окна

        :param type_of_window: Тип окна

        :return: Коэффициент сопротивления теплопередаче

        Примеры:
        >>> window = Window(1600, 1600)
        >>> window.init_coefficient_of_heat_transfer_resistance("A1")
        """
        ...

class Roof:
    """
    Класс описывает модель крыши
    """
    def __init__(self, type: str, base_length: Union[int, float], base_width: Union[int, float], height: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Окно"

        :param type: Тип крыши
        :param base_length: Длина основания
        :param base_width: Ширина основания
        :param height: Высота крыши

        Примеры:
        >>> roof = Roof("двускатная", 10000, 16000, 3000)  # инициализация экземпляра класса
        """
        if not isinstance(base_length, (int, float)):
            raise TypeError
        if not base_length > 0:
            raise ValueError
        self.base_length = base_length

        if not isinstance(base_width, (int, float)):
            raise TypeError
        if not base_width > 0:
            raise ValueError
        self.base_width = base_width

        if not isinstance(height,(int, float)):
            raise TypeError
        if not height > 0:
            raise ValueError
        self.height = height

    def calculate_roof_area(self, type: str, base_length: Union[int, float], base_width: Union[int, float], height: Union[int, float]) -> Union[int, float]:
        """
        Функция, которая вычисляет площадь кровли

        :param type: Тип крыши
        :param base_length: Длина основания
        :param base_width: Ширина основания
        :param height: Высота крыши

        :return: Площадь кровли
        """
        ...

    def calculate_of_angle_of_inclination(self, base_length: Union[int, float], base_width: Union[int, float], height: Union[int, float]) -> float:
        """
        Функция, которая вычисляет угол наклона стропильной системы двускатной крыши

        :param base_length: Длина основания
        :param base_width: Ширина основания
        :param height: Высота крыши

        :return: Угол наклона
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
