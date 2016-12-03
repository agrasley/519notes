from __future__ import division
from math import sqrt, floor


def memoize(f):
    d = dict()

    def wrapper(*args):
        if args in d:
            return d[args]
        else:
            result = f(*args)
            d[args] = result
            return result

    return wrapper


def squares(n):
    m = floor(sqrt(n))

    @memoize
    def s(x, i):
        if x == 0:
            return 0
        elif i < 1:
            return float("inf")
        elif x == i**2:
            return 1
        else:
            return min([s(x-(y * i**2), i-1) + y for y in xrange(x//(i**2)+1)])

    return s(n, int(m))
