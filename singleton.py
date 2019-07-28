#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class Singleton(object):
#     _instance = None
#     def __new__(cls, *args, **kw):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
#         return cls._instance
#
#
# class MyClass(Singleton):
#     a = 1


"""
# 天然单例模式
class My_Singleton(object):
    def foo(self):
        pass
my_singleton = My_Singleton()

from mysingleton import my_singleton
my_singleton.foo()
"""

from functools import wraps
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1

if __name__ == '__main__':
    a =   MyClass()
    b = MyClass()
    print(id(a))
    print(id(b))