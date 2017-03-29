import functools
from re import search


def Map():
    pass


def Filter():
    pass


def Reduce():
    pass


class Enumerable:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return self._iterable.__iter__()

    def filter(self, func, *args, **kwargs):
        return Filter(self._iterable, func, *args, **kwargs)

    def map(self, func, *args, **kwargs):
        return Map(self._iterable, func, *args, **kwargs)

    def reduce(self, func, *args, **kwargs):
        return Reduce(self._iterable, func, *args, **kwargs)

    def to(self, container_type):
        return container_type(self._iterable)


def Filter(iterable, func, *args, **kwargs):
    return Enumerable((x for x in iterable if func(x, *args, **kwargs)))


def Map(iterable, func, *args, **kwargs):
    return Enumerable((func(x, *args, **kwargs) for x in iterable))


def Reduce(iterable, func, initializer=0, *args, **kwargs):
    def reduce_func(accumulator, value):
        return func(accumulator, value, *args, **kwargs)

    return functools.reduce(reduce_func, iterable, initializer)
