from random import randint
from heapq import heappop, heappush


def _is_lt(a, b):
    if a[0] + a[1] < b[0] + b[1] or (a[0] + a[1] == b[0] + b[1] and a[1] < b[1]):
        return True
    else:
        return False


def _qsort_cartesian(a):
    if a == []:
        return []
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if _is_lt(x, pivot)]
        right = [x for x in a[1:] if not _is_lt(x, pivot)]
        return _qsort_cartesian(left) + [pivot] + _qsort_cartesian(right)


def _qsort(a):
    if a == []:
        return []
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return _qsort(left) + [pivot] + _qsort(right)


def _qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if _is_lt(x, pivot)]
        right = [x for x in a[1:] if not _is_lt(x, pivot)]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            _qselect(k, left) if k <= lleft else \
            _qselect(k-lleft-1, right)


def nbesta(a, b):
    if len(a) != len(b):
        return None
    if a == []:
        return []
    c = [(x, y) for x in a for y in b]
    return _qsort_cartesian(c)[:len(a)]


def nbestb(a, b):
    if len(a) != len(b):
        return None
    if a == []:
        return []
    c = [(x, y) for x in a for y in b]
    selection = _qselect(len(a), c)
    z = [x for x in c if _is_lt(x, selection)]
    z = _qsort_cartesian(z)
    z.extend([selection] * (len(a) - len(z)))
    return z


def _prioritize(h, results, a, b, c):
        root = heappop(h)
        results.append((a[root[2]], b[root[3]]))
        if len(results) == len(a):
            return
        else:
            if not (root[2] + 1, root[3]) in c:
                heappush(h, (a[root[2]+1] + b[root[3]], b[root[3]], root[2] + 1, root[3]))
                c.add((root[2] + 1, root[3]))
            if not (root[2], root[3] + 1) in c:
                heappush(h, (a[root[2]] + b[root[3]+1], b[root[3]+1], root[2], root[3]+1))
                c.add((root[2], root[3] + 1))
            _prioritize(h, results, a, b, c)


def nbestc(a, b):
    if len(a) != len(b):
        return None
    if a == []:
        return []
    results = []
    y, z = _qsort(a), _qsort(b)
    h = [(y[0]+z[0], z[0], 0, 0)]
    _prioritize(h, results, y, z, {(0, 0)})
    return results


if __name__ == '__main__':
    import unittest
    import time

    def random_list(start, stop, size):
        return [randint(start, stop) for _ in xrange(size)]

    class TestNBest(unittest.TestCase):

        def test_base_cases(self):
            self.assertEqual(nbesta([], []), [])
            self.assertEqual(nbestb([], []), [])
            self.assertEqual(nbestc([], []), [])
            self.assertIs(nbesta([1], []), None)
            self.assertIs(nbestb([1], []), None)
            self.assertIs(nbestc([1], []), None)

        def test_random_lists(self):
            a = random_list(-15, 15, 25)
            b = random_list(-5, 20, 25)
            self.assertEqual(nbesta(a, b), nbestb(a, b))
            self.assertEqual(nbestb(a, b), nbestc(a, b))

        def test_instructor_examples(self):
            a, b = [4, 1, 5, 3], [2, 6, 3, 4]
            result = [(1, 2), (1, 3), (3, 2), (1, 4)]
            self.assertEqual(nbesta(a, b), result)
            self.assertEqual(nbestb(a, b), result)
            self.assertEqual(nbestc(a, b), result)

        def test_execution_speeds(self):
            a = random_list(0, 25, 25)
            b = random_list(0, 25, 25)
            nbesta_t0 = time.clock()
            nbesta(a, b)
            nbesta_t1 = time.clock() - nbesta_t0
            nbestb_t0 = time.clock()
            nbestb(a, b)
            nbestb_t1 = time.clock() - nbestb_t0
            nbestc_t0 = time.clock()
            nbestc(a, b)
            nbestc_t1 = time.clock() - nbestc_t0
            self.assertLess(nbestb_t1, nbesta_t1)
            self.assertLess(nbestc_t1, nbestb_t1)

    unittest.main()
