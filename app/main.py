"""
Modul description
"""

from typing import Union
import math
from app.error import InvalidInputException

numeric = Union[int, float]


class Calculator:
    """
    class Calculator description
    """
    @staticmethod
    def sum(*args):
        """
        Function "sum" description
        """
        for arg in args:
            if not isinstance(arg, numeric):
                raise TypeError
        return sum(args)

    @staticmethod
    def subtract(a: numeric, b: numeric) -> numeric:
        """
        Function "subtract" description
        """
        return a - b

    @staticmethod
    def multiply(a: numeric, b: numeric) -> numeric:
        """
        Function "multiply" description
        """
        return a * b

    @staticmethod
    def divide(a: numeric, b: numeric) -> numeric:
        """
        Function "divide" description
        """
        return a / b

    def log(self, a: numeric, base: numeric) -> numeric:
        """
        Function "log" description
        """
        if not (isinstance(a, numeric) and isinstance(base, numeric)):
            raise TypeError

        #if a > 0 and a != 1 and base > 0:           # a != 1 - лишнее
        if a > 0 and base > 0:
            return math.log(a, base)
        else:
            raise InvalidInputException(self.log, a, base)


calc = Calculator()

# проверка что все класс работает - OK
# print('проверка 6 + 2 = ', calc.sum(6, 2))       #8
# print('проверка 6 : 2 = ', calc.divide(6, 2))    #3.0
# print('проверка 6 * 2 = ', calc.multiply(6, 2))  #12
# print('проверка log2-8 = ', calc.log(8, 2))    #3

#d = calc.log('a', 0)
#print(d) # здесь будет ошибка

