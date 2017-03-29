from functools import reduce


class Enumerable:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return self._iterable.__iter__()

    def filter(self, func, *args, **kwargs):
        return Enumerable((x for x in self._iterable if func(x, *args, **kwargs)))

    def map(self, func, *args, **kwargs):
        return Enumerable((func(x, *args, **kwargs) for x in self._iterable))

    def reduce(self, func, initializer=0, *args, **kwargs):
        def reduce_func(accumulator, value):
            return func(accumulator, value, *args, **kwargs)

        return reduce(reduce_func, self._iterable, initializer)

    def to(self, container_type):
        return container_type(self._iterable)


def Filter(iterable, func, *args, **kwargs):
    return Enumerable(iterable).filter(func, *args, **kwargs)


def Map(iterable, func, *args, **kwargs):
    return Enumerable(iterable).map(func, *args, **kwargs)


def Reduce(iterable, func, initializer=0, *args, **kwargs):
    return Enumerable(iterable).reduce(func, initializer, *args, **kwargs)