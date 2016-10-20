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


def naive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return naive_fib(n-1) + naive_fib(n-2)


@memoize
def memoized_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fib(n-1) + memoized_fib(n-2)
