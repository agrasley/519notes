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


def lis(s):
    s = 'Z' + s + '{'

    @memoize
    def l(i):
        if i < 1:
            return 0, s[0]
        else:
            return max([(l(j)[0] + 1, j) for j in xrange(i) if s[j] < s[i]])

    backtrace_results = []

    def backtrace(i):
        _, j = l(i)
        if j > 0:
            backtrace_results.append(s[j])
            backtrace(j)

    backtrace(len(s) - 1)
    backtrace_results.reverse()
    return ''.join(backtrace_results)
