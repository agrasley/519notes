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
        print "calculating", n
        return naive_fib(n-1) + naive_fib(n-2)


def memoized_fib(n):

    @memoize
    def f(n):
        print "calculating ", n
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return f(n-1) + f(n-2)

    return f(n)


@memoize
def fib(n):
    print "calculating ", n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):

    def helper_fib(n, cache={}):
        if n in cache:
            return cache[n]
        print 'calculating', n
        if n < 2:
            cache[n] = 1
            return 1
        else:
            result = helper_fib(n-1, cache) + helper_fib(n-2, cache)
            cache[n] = result
            return result

    return helper_fib(n)
