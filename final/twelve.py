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


def bool_exp(s):

    @memoize
    def f(i, j):
        if j - i == 1:
            if s[i] == 'F':
                return 1
            else:
                return 0
        else:
            total = 0
            for k in xrange(i+1, j):
                if s[k] == '|':
                    total += f(i, k) * f(k+1, j)
                elif s[k] == '&':
                    total += t(i, k) * f(k+1, j)
                    total += f(i, k) * t(k+1, j)
                    total += f(i, k) * f(k+1, j)
            return total

    @memoize
    def t(i, j):
        if j - i == 1:
            if s[i] == 'T':
                return 1
            else:
                return 0
        else:
            total = 0
            for k in xrange(i+1, j):
                if s[k] == '|':
                    total += t(i, k) * f(k+1, j)
                    total += f(i, k) * t(k+1, j)
                    total += t(i, k) * t(k+1, j)
                elif s[k] == '&':
                    total += t(i, k) * t(k+1, j)
            return total

    return t(0, len(s))
