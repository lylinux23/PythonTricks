#   -*- coding:utf-8 -*-
# @Time    : 2022/3/17 上午11:52
# @Author  : Youliang Luo
# @FileName: C2 Patterns for Cleaner Python.py
# @Software: PyCharm
# @Project : Python Tricks

# 2.1 Covering Your A** With Assertions
# What are assertions and what are they good for?

shoes = {'name': 'Fancy Shoes', 'price': 999}

def ApplyDiscount(product:str, discount:float) -> int:
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']

    return price

ApplyDiscount(shoes, 0.25)

'''
    Python's assert statement is a debugging aid, not a mechanism for handing run-time errors.
'''

# assert(1 == 2, 'This should fail')

'''
    Key Takeaways
    1. Python's assert statement is a debugging aid that tests a condition as an internal self-check in your program
    2. Asserts should only be used to help developers identify bugs.
    3. Asserts can be globally disabled with an interpreter setting.
'''

# 2.2 Complacent Comma Placement
names1 = [
    'Alice',
    'Bob',
    'Dirk',
    'Jane',
]

names2 = [
    'Alice',
    'Bob',
    'Dirk'
    'Jane'
]


