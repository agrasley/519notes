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
            return 0
        else:
            x = helper(length-2)
            y = helper(length-1)
            return max(a[length-1] + x, x, y)

    result = helper(len(a))

    path = []
    i = len(a)
    while i > 0:
        if helper(i - 1) > helper(i - 2) + a[i-1]:
            i -= 1
        else:
            path.append(a[i-1])
            i -= 2

    path.reverse()
    return result, path


def max_wis2(a):
    results = [0, 0]
    i = 2
    while i < len(a) + 2:
        x = results[i-2]
        y = results[i-1]
        results.append(max(x + a[i-2], x, y))
        i += 1

    path = []
    i = len(results)
    while i-2 > 0:
        if results[i-2] > results[i-3] + a[i-3]:
            i -= 1
        else:
            path.append(a[i-3])
            i -= 2

    path.reverse()
    return results[-1], path
