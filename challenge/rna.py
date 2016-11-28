from heapq import heapify, heappop, heappush
from itertools import islice
from random import randint
from numbers import Number


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

pairs = frozenset(['AU', 'GC', 'GU', 'UA', 'CG', 'UG'])


def _qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            _qselect(k, left) if k <= lleft else \
            _qselect(k-lleft-1, right)


def best(s):

    @memoize
    def b(i, j):
        if j - i < 2:
            return 0, False, None
        else:
            m = 0, False, None
            if s[i] + s[j-1] in pairs:
                m = b(i+1, j-1)[0] + 1, True, None
            for k in xrange(i+1, j):
                if b(i, k)[0] + b(k, j)[0] > m[0]:
                    m = b(i, k)[0] + b(k, j)[0], False, k
            return m

    backtrace_results = ['.'] * len(s)

    def backtrace(i, j):
        _, x, k = b(i, j)
        if x:
            backtrace_results[i] = '('
            backtrace_results[j-1] = ')'
            backtrace(i+1, j-1)
        elif k is not None:
            backtrace(i, k)
            backtrace(k, j)

    backtrace(0, len(s))

    return b(0, len(s))[0], ''.join(backtrace_results)


def total(s):

    @memoize
    def t(i, j):
        if j - i < 2:
            return 1
        else:
            tot = 0
            for k in xrange(i+1, j):
                if s[i] + s[k] in pairs:
                    tot += t(i+1, k) * t(k+1, j)
            return tot + t(i+1, j)

    return t(0, len(s))


def kbest(s, kth):
    iterDict = {}
    gens = {}

    def iter8(i, j, n):
        if (i, j, n) in iterDict:
            return iterDict[(i, j, n)]
        if (i, j) in gens:
            gen, cntr = gens[(i, j)]
        else:
            gen, cntr = kb(i, j), 0
        while cntr is not None and cntr <= n:
            try:
                res = gen.next()
                iterDict[(i, j, cntr)] = res
                cntr += 1
            except StopIteration:
                cntr = None
        gens[(i, j)] = (gen, cntr)
        if cntr is None:
            return None, None
        else:
            return iterDict[(i, j, n)]

    def kb(i, j):
        if j - i < 2:
            yield 0, None
        else:
            h, used = [], set()

            def trypush(k, ni, nj):
                cand1, _ = iter8(i+1, k, ni)
                cand2, _ = iter8(k+1, j, nj)
                if cand1 is not None and cand2 is not None and (k, ni, nj) not in used:
                    heappush(h, (-(cand1 + cand2 + 1), k, ni, nj))
                    used.add((k, ni, nj))

            for k in xrange(i+1, j):
                if s[i] + s[k] in pairs:
                    h.append((-(iter8(i+1, k, 0)[0] + iter8(k+1, j, 0)[0] + 1), k, 0, 0))
                    used.add((k, 0, 0))
            h.append((-(iter8(i+1, j, 0)[0]), None, 0, None))
            if len(h) > kth:
                pivot = _qselect(kth, h)
                new_h = []
                for x in h:
                    if x < pivot:
                        new_h.append(x)
                new_h.append(pivot)
                h = new_h
            heapify(h)
            while len(h):
                val, k, ni, nj = heappop(h)
                if k is not None:
                    yield -(val), (k, ni, nj)
                    trypush(k, ni+1, nj)
                    trypush(k, ni, nj+1)
                else:
                    yield -(val), ni
                    cand, _ = iter8(i+1, j, ni+1)
                    if cand is not None:
                        heappush(h, (-cand, None, ni+1, None))

    def backtrace(i, j, x):
        backtrace_results = ['.'] * len(s)

        def bt(i, j, x):
            if x is None:
                return
            elif isinstance(x, Number):
                _, new_x = iter8(i+1, j, x)
                bt(i+1, j, new_x)
            else:
                k, ni, nj = x
                backtrace_results[i] = '('
                backtrace_results[k] = ')'
                _, new_x = iter8(i+1, k, ni)
                bt(i+1, k, new_x)
                _, new_x = iter8(k+1, j, nj)
                bt(k+1, j, new_x)

        bt(i, j, x)
        return ''.join(backtrace_results)

    results = []

    for v, x in islice(kb(0, len(s)), kth):
        results.append((v, backtrace(0, len(s), x)))

    return results
