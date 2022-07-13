#   -*- coding:utf-8 -*-
# @Time    : 2022/7/13 上午11:48
# @Author  : Youliang Luo
# @FileName: 04 Docstings.py
# @Software: PyCharm
# @Project : PythonTricks

"""
Use comments to explain how code works. Comments are great for leaving notes for people working on your program.
Docstrings provide documentation about functions, classes, and modules.
Use docstrings to teach other developers how to use your program
"""

def every_other(lst):
    """([int]) -> [int]
    Get every other element of the list.
    :param lst:
    :return: lst
    """

    return lst[::2]

help(every_other)

class Calculator:
    """
    This is a simple calculator.
    """

    def add(self, a, b):
        """(float, float) -> float

        a: first number
        b: second number
        requirement: a >= 0, b >= 0
        return: sum of a and b >= 0

        Add 2 numbers

        >>> t = Calculator()
        >>> t.add(2, 4)
        6


        >>> t.add(-2, 4)
        Traceback (most recent call last):
        ...
        ValueError: input numbers should be greater than zero.

        """

        if a < 0 or b <0:
            raise ValueError('Input numbers should be greater than zero')

        return a + b