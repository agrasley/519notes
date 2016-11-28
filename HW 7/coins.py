from __future__ import division


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


def best(x, vs):

    @memoize
    def b(x, i):
        if x == 0:
            return 0, 0
        elif i >= len(vs):
            return None, None
        else:
            vi = vs[i]
            for j in xrange(x // vi + 1):
                res, _ = b(x-vi*j, i+1)
                if j == 0:
                    minimum, jbest = res, j
                elif res is not None and (minimum is None or minimum >= res+1):
                    minimum, jbest = res + 1, j
            return minimum, jbest

    res = b(x, 0)

    if res[0] is None:
        return None

    backtrace_results = [0] * len(vs)

    def backtrace(x, i):
        minimum, j = b(x, i)
        backtrace_results[i] = j
        if x-vs[i]*j != 0:
            backtrace(x-vs[i]*j, i+1)

    backtrace(x, 0)

    return res[0], backtrace_results
