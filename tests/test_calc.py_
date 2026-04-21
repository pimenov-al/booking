"""
Modul description
"""

import math
import unittest
from math import inf
from parameterized import parameterized
from app.main import Calculator

# список импортов в видео воркшопа см на время 33:33


class TestCalculator(unittest.TestCase):
    """
    Модуль для тестирования функции логарифма
    """
    # здесь запускаем один экз app на все тесты
    def setUp(self) -> None:
        """
        Описание функции setUp
        """
        self.calc = Calculator()

    # здесь все зачищаем после отработки тестов
    def tearDown(self) -> None:
        """
        Описание функции tearDown
        """
        #...


    @parameterized.expand(
        # 1. arrange
        # задаем варианты параметров (a,b, ожид.рез)
        # для каждого теста, который идет дальше
        # как это (@parameterized.expand) попадает в тест (def test_sum) ????
        [
            ("integers", 2, 3, 5),
            ("floats", 2.5, 3.1, 5.6),
            ("negative", -2.5, 3.0, 0.5)
        ]
    )
    #def test_sum(self, name, a, b, expected_result):
    def test_sum(self, a, b, expected_result):
        """
        Описание функции test_sum
        """
        # 2. act
        # получаем факт. результат выполнения функции
        actual_result = self.calc.sum(a, b)

        # 3. assert
        # сравниваем факт. и ожидаемый результаты
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("strings", 'aaa', 'bbb', TypeError),
        ("int_None", 1, None, TypeError),
        ("None_float", None, 1.1, TypeError),
        ("None_None", None, None, TypeError)

    ])
    #def test_sum_invalid_values(self, name, a, b, expected_result):
    def test_sum_invalid_values(self, a, b, expected_result):
        """
        Описание функции test_sum_invalid_values
        """
        with self.assertRaises(expected_result):
            self.calc.sum(a, b)

    @parameterized.expand([
        ("list_integers", [1, 2, 3, 4], 10),
        ("list_empty", [], 0),
        ("list_single", [1], 1)
    ])
    #def test_sum_list(self, name, a, expected_result):
    def test_sum_list(self, a, expected_result):
        """
        Описание функции test_sum_list
        """
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ("tuple_integers", (1, 2, 3, 4), 10),
        ("tuple_empty", (), 0),
        ("tuple_single", (1,), 1),
        ("set_integers", {1, 2, 3, 4}, 10),
        ("set_empty", {}, 0),
        ("set_single", {1}, 1),
    ])
    #def test_sum_tuple(self, name, a, expected_result):
    def test_sum_tuple(self, a, expected_result):
        """
        Описание функции test_sum_tuple
        """
        # 2. act
        actual_result = self.calc.sum(*a)
        # 3. assert
        self.assertEqual(actual_result, expected_result)

    def test_multiply(self):
        """
        Описание функции test_multiply
        """
        a = 5
       # b = 0 # OK
        b = 0.000000005 #failed

        actual_result = self.calc.multiply(a, b)
        expected_result = 0 # OK, = 1 # failed
        # self.assertEqual(actual_result, expected_result) # для b = 0.00000000
        # тест будет failed, т.к. резалт будет не ровный ноль, нужен assertAlmostEqual

        self.assertAlmostEqual(actual_result, expected_result) # OK
        #здесь по дефолту сравниваются числа до 7 знака, places может изменить это
        #self.assertAlmostEqual(actual_result, expected_result, places=8) # так упадет

    def test_divide(self):
        """
        Описание функции test_divide
        """
        a = 5
        b = 0

        expected_result = ZeroDivisionError

        with self.assertRaises(expected_result):
            self.calc.divide(a, b)

    def test_divide_inf(self):
        """
        Описание функции test_divide_inf
        """
        a = inf
        b = inf

        expected_result = None
        actual_result = self.calc.divide(a, b)

        self.assertNotEqual(actual_result, expected_result)
        self.assertIsInstance(actual_result, type(math.inf))
        self.assertIsInstance(actual_result, float)

# это наш ранер
if __name__ == "__main__":
    unittest.main()
