#   -*- coding:utf-8 -*-
# @Time    : 2022/5/5 上午9:14
# @Author  : Youliang Luo
# @FileName: 03 Tricks.py
# @Software: PyCharm
# @Project : PythonTricks


# Trick 001
print('-'*30,'Trick 001 Begin', '-'*30)
"""
    More than ONE input
"""

x, y, z= input('Input Three Numbers:').split()
print(f'x is {x}')
print(f'y is {y}')
print(f'z is {z}')

print('-'*30, 'Trick 001 Done ', '-'*30)


# TRICK 002
'''
    Conditional Judgement
'''
print('-'*30,'Trick 002 Begin', '-'*30)
subs = 200
likes = 100
comments = 50

if(subs > 100 and likes > 50 and comments > 25):
    print('Awesome film!')


# A Better Way to Implement it.
conditions = [subs > 100,
              likes > 50,
              comments > 25]

if all(conditions):
    print('A Better Way to express: Awesome film')

print('-'*30, 'Trick 002 Done ', '-'*30)



# Trick 003

print('-'*30,'Trick 003 Begin', '-'*30)

"""
    Reversing a string in Python
"""

AString = 'GeeksForGeeks'
print('Reverse is', AString[::-1])


print('-'*30, 'Trick 003 Done ', '-'*30)

# Trick 004
print('-'*30,'Trick 004 Begin', '-'*30)
"""
    Create a single string from all the elements in list
"""
a = ["Way", "to", "go", "maotao"]
print(" ".join(a))

print('-'*30, 'Trick 004 Done ', '-'*30)


# Trick 005
print('-'*30,'Trick 005 Begin', '-'*30)
"""
    Check The Memory Usage Of An Object.
"""

import sys
AString = 'Way to go!'
print(f'Size of AString: {sys.getsizeof(AString)}')

print('-'*30, 'Trick 005 Done ', '-'*30)


# Trick 006
print('-'*30,'Trick 006 Begin', '-'*30)
"""
    Get the difference between the two Lists
    
"""
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

# We want output like this list3 = ['Emma', 'Smith]

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(f'Get the difference between list1 and list2: {list3}')

print('-'*30, 'Trick 006 Done ', '-'*30)

# Trick 007
print('-'*30,'Trick 007 Begin', '-'*30)
"""
    Merge two dictionaries in a single expression
"""
currentEmployee = {1: 'Scott', 2: "Eric", 3:"Kelly"}
formerEmployee  = {2: 'Eric', 4: "Emma"}

allEmployee = {**currentEmployee, **formerEmployee}
print(f'Merge two dictionaries {allEmployee}')

print('-'*30, 'Trick 007 Done ', '-'*30)

# Trick 008
print('-'*30,'Trick 008 Begin', '-'*30)
"""
    AIM: Convert two lists into a dictionary
    one list contains keys and the second contains values
    convert those two lists into a single dictionary
"""
ItemId = [1, 2, 3]
names = ["Hard Disk", "Laptop", "RAM"]

itemDictionary = dict(zip(ItemId, names))
print(f'Convert two lists into a dictionary. {itemDictionary}')

print('-'*30, 'Trick 008 Done ', '-'*30)




##################################################
# Trick ???
print('-'*30,'Trick 00? Begin', '-'*30)
"""
    xxxx
"""

print('-'*30, 'Trick 00? Done ', '-'*30)
####################################################




# Trick ???
print('-'*30,'Trick 00? Begin', '-'*30)
"""
    More than ONE input
"""

print('-'*30, 'Trick 00? Done ', '-'*30)