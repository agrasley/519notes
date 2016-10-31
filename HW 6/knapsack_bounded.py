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


def second_best(weight, items):

    @memoize
    def b(weight, i):
        return (0, None) if i >= len(items) else max([(b(weight-items[i][0]*j, i+1)[0] + items[i][1]*j, j) for j in xrange(items[i][2]+1) if items[i][0]*j <= weight])

    results = b(weight, 0)
    backtrace_results = [0] * len(items)

    def backtrace(weight, i):
        if i >= len(items):
            return
        else:
            (_, j) = b(weight, i)
            backtrace_results[i] = j
            backtrace(weight-items[i][0]*j, i+1)

    backtrace(weight, 0)

    return results[0], backtrace_results


def best(weight, items):
    total_weight = 0
    total_price = 0
    for (w, p, n) in items:
        total_weight += w*n
        total_price += p*n
    if total_weight <= weight:
        return total_price, [n for (_, _, n) in items]
    items = sorted(enumerate(items), key=lambda item: item[1][1]//item[1][0])  # sort items in increasing price/weight
    dp = [[0 for _ in xrange(len(items)+1)] for _ in xrange(weight+1)]  # initialize results matrix
    backtrace = [[None for _ in xrange(len(items)+1)] for _ in xrange(weight+1)]
    delta = [None for _ in xrange(weight+1)]

    def insert(s, d):
        while s != [] and delta[s[-1]] >= delta[d]:
            s.pop()
        s.append(d)

    for i in xrange(1, len(items)+1):
        pi, wi, bi = items[i-1][1][1], items[i-1][1][0], items[i-1][1][2]
        for d in xrange(weight+1):
            delta[d] = d*pi//wi - dp[d][i-1]
        for r in xrange(wi):
            d0 = r
            d = r + wi
            k = 1
            s = []
            while d <= weight:
                if dp[d][i-1] < dp[d0][i-1] + k * pi:
                    dp[d][i] = dp[d0][i-1] + k * pi
                    backtrace[d][i] = (k, items[i-1][0])
                    insert(s, d)
                    d = d + wi
                    if k < bi:
                        k += 1
                    else:
                        d0 = s.pop(0)
                        k = (d-d0)/wi
                else:
                    dp[d][i] = dp[d][i-1]
                    backtrace[d][i] = (0, items[i-1][0])
                    d0 = d
                    k = 1
                    d = d + wi
                    s = []

    backtrace_results = [0 for _ in xrange(len(items))]

    def back(weight, row):
        if row <= 0:
            return
        else:
            k, i = backtrace[weight][row]
            backtrace_results[i] = k
            back(weight - items[row-1][1][0] * k, row-1)

    back(weight, len(items))

    return dp[-1][-1], backtrace_results
