from heapq import heapify, heappop, heappush
from itertools import islice

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
            q = tot + t(i+1, j)
            return q

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
            return None
        else:
            return iterDict[(i, j, n)]

    def kb(i, j):
        if j - i < 2:
            yield 0
        else:
            h, used = [], set()

            def trypush(k, ni, nj):
                cand1 = iter8(i+1, k, ni)
                cand2 = iter8(k+1, j, nj)
                if cand1 is not None and cand2 is not None and (k, ni, nj) not in used:
                    heappush(h, (-(cand1 + cand2 + 1), k, ni, nj))
                    used.add((k, ni, nj))

            for k in xrange(i+1, j):
                if s[i] + s[k] in pairs:
                    h.append((-(iter8(i+1, k, 0) + iter8(k+1, j, 0) + 1), k, 0, 0))
                    used.add((k, 0, 0))
            h.append((-(iter8(i+1, j, 0)), None, 0, None))
            heapify(h)
            while len(h):
                val, k, ni, nj = heappop(h)
                yield -(val)
                if k is not None:
                    trypush(k, ni + 1, nj)
                    trypush(k, ni, nj + 1)
                else:
                    cand = iter8(i+1, j, ni+1)
                    if cand is not None:
                        heappush(h, (-cand, None, ni+1, None))

    return list(islice(kb(0, len(s)), kth))


print best("UUCAGGA")  # 3
print best("GUUAGAGUCU")  # 4
print best("GCACG")  # 2
print best("AUAACCUUAUAGGGCUCUG")  # 8
print best("UUGGACUUGAGAAAAG")  # 5
print best("UCAAUGGGUAGUAAAU")  # 6
print best("UUUGGCACUUUCAGA")  # 6
print best("ACACACCUUGUCCGUGAA")  # 6
print best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG")  # 14
print best("CGCGAAUAAAAAGGCACUGUU")  # 8
print best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC")  # 19
print best("UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU")  # 15
print best("AUACGUCGGGGACAAGAAUUACGG")  # 8
print best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA")  # 20
print best("CGAGGUGGCACUGACCAAACACCACCGAAAC")  # 9
print best("CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU")  # 12
print best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")  # 18
print best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")  # 11
print best("")  # 0
