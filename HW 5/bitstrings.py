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


def num_no(n):

    @memoize
    def nn(n):
        if n == 0:
            return 1
        elif n == 1:
            return 2
        elif n == 2:
            return 3
        else:
            return nn(n-1) + nn(n-2)

    return nn(n)


def num_yes(n):
    return 2**n - num_no(n)
