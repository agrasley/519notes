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

# a = [{1: 2, 3: 5}, {0: 2, 2: 3}, {1: 3, 3: 2}, {0: 5, 2: 2}]

'''
def ham_cycle(adj_list):

    @memoize
    def path(s, v):
        if len(s) == 1:
            if v in adj_list[0]:
                return True
            else:
                return False
        else:
            s_ = s-frozenset([v])
            for x in s_:
                if path(s_, x):
                    return True
            return False

    for x in adj_list[0]:
        if path(frozenset(range), x):
'''


def tsp(adj_list):

    @memoize
    def d(s, c):
        if len(s) == 1:
            if c in adj_list[0]:
                return adj_list[0][c], 0
            else:
                return float("inf"), None
        else:
            s_ = s-frozenset([c])
            cand = [(d(s_, x)[0] + adj_list[c][x], x) for x in adj_list[c] if x in s_]
            return min(cand) if len(cand) else (float("inf"), None)

    s = frozenset(range(1, len(adj_list)))
    l, c = min([(d(s, c)[0] + adj_list[0][c], c) for c in adj_list[0]])

    backtrace_results = [0, c]

    def backtrace(s, c):
        _, c_ = d(s, c)
        backtrace_results.append(c_)
        s_ = s-frozenset([c])
        if len(s_):
            backtrace(s_, c_)

    backtrace(s, c)
    return l, backtrace_results

print tsp([{1: 2, 3: 5}, {0: 2, 2: 3}, {1: 3, 3: 2}, {0: 5, 2: 2}])
print tsp([{1: 10, 3: 5}, {0: 10, 2: 3}, {1: 3, 3: 2}, {0: 5, 2: 2}])
print tsp([{1: 2, 2: 4}, {0: 2, 2: 1}, {0: 4, 1: 1}])
