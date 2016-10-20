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


def max_wis(a):

    @memoize
    def helper(length):
        if length < 1:
            return (0, [])
        else:
            x = helper(length-2)
            x1 = x[1][:]
            x1.append(a[length-1])
            y = helper(length-1)
            return max((a[length-1] + x[0], x1), x, y)

    return helper(len(a))


def max_wis2(a):
    x = y = z = (0, [])
    for item in a:
        new_y = z
        new_x = max(y, x)
        if item < 0:
            new_z = new_x
        else:
            new_z = (new_x[0]+item, new_x[1] + [item])
        x, y, z = new_x, new_y, new_z
    return max(y, z)
