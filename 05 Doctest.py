#   -*- coding:utf-8 -*-
# @Time    : 2022/7/13 下午12:41
# @Author  : Youliang Luo
# @FileName: 05 Doctest.py
# @Software: PyCharm
# @Project : PythonTricks

def every_other(lst):
    """([int]) -> [int]
    Get every other element of the list.

    >>> every_other([1, 2, 3, 4, 5, 6])
    [1, 3, 5]

    >>> every_other([2, 5, 7, 0, 8, 10])
    [2, 7, 8]

    """

    return lst[::2]

import doctest
doctest.testmod()