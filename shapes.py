from abc import ABC, abstractmethod
from math import pi, sqrt


DEFAULT_PRECISION = 3


class Shape(ABC):
    """Абстрактный класс Фигуры"""

    shape_name = ''

    def __init__(self, precision: int) -> None:
        self.precision = precision

    @abstractmethod
    def _raw_area(self) -> float:
        pass

    @staticmethod
    def _validate_negative_values(*args: float | int) -> None:
        if any(map(lambda x: x < 0, args)):
            raise ValueError(
                'Отрицательное число не может быть значением фигуры')

    @property
    def area(self) -> float:
        return round(self._raw_area(), self.precision)

    def __str__(self) -> str:
        return f'{self.shape_name}, параметры: {self.__dict__}, площадь: {self.area}.'


class Circle(Shape):
    """Окружность"""

    shape_name = 'Окружность'

    def __init__(self,
                 radius: float,
                 precision: int = DEFAULT_PRECISION) -> None:
        self._validate_negative_values(radius, precision)
        super().__init__(precision)
        self.radius = radius

    def _raw_area(self) -> float:
        return pi * self.radius ** 2


class Rectangle(Shape):
    """Прямоугольник"""

    shape_name = 'Прямоугольник'

    def __init__(self,
                 side_1: float,
                 side_2: float,
                 precision: int = DEFAULT_PRECISION) -> None:
        self._validate_negative_values(side_1, side_2, precision)
        super().__init__(precision)
        self.side_1 = side_1
        self.side_2 = side_2

    def _raw_area(self) -> float:
        return self.side_1 * self.side_2


class Square(Shape):
    """Квадрат"""

    shape_name = 'Квадрат'

    def __init__(self,
                 side: float,
                 precision: int = DEFAULT_PRECISION) -> None:
        self._validate_negative_values(side, precision)
        super().__init__(precision)
        self.side = side

    def _raw_area(self) -> float:
        return self.side ** 2


class Triangle(Shape):
    """Треугольник"""

    shape_name = 'Треугольник'

    def __init__(self,
                 side_a: float,
                 side_b: float,
                 side_c: float,
                 precision: int = DEFAULT_PRECISION) -> None:
        self._validate_negative_values(side_a, side_b, side_c, precision)
        self._validate_triangle(side_a, side_b, side_c)
        super().__init__(precision)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.is_triangle_right = self._is_triangle_right(
            side_a, side_b, side_c)

    @staticmethod
    def _validate_triangle(a: float, b: float, c: float) -> None:
        if a + b > c and b + c > a and c + a > b:
            return
        raise ValueError('Такой треугольник невозможен')

    @staticmethod
    def _is_triangle_right(a: float, b: float, c: float) -> bool:
        a, b, c = sorted([a, b, c])
        is_triangle_right = (a ** 2 + b ** 2 - c ** 2) < 1e-9
        return is_triangle_right

    def _raw_area(self) -> float:
        a, b, c = self.side_a, self.side_b, self.side_c
        semi_per = (a + b + c) / 2
        area = sqrt(semi_per * (semi_per - a) *
                    (semi_per - b) * (semi_per - c))
        return area
