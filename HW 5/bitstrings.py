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


@memoize
def num_no(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return num_no(n-1) + num_no(n-2)


def num_yes(n):
    return 2**n - num_no(n)
