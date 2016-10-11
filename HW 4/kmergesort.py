from heapq import heapify, heapreplace, heappop


def _mergesort(k):
    def _m(x):
        if len(x) < k:
            return _merge(map((lambda y: [y]), x))
        else:
            i = 0
            results = [[] for _ in xrange(k)]
            while i < len(x):
                results[i % k].append(x[i])
                i += 1
            return _merge(map(_m, results))
    return _m


def _merge(a):
    results = []
    e = enumerate(map(list, map(enumerate, a)))
    h = [(y[0][1], x, y[0][0]) for (x, y) in e]
    heapify(h)
    while len(h) > 0:
        root_val, root_list, root_idx = h[0]
        results.append(root_val)
        if root_idx + 1 < len(a[root_list]):
            heapreplace(h, (a[root_list][root_idx+1], root_list, root_idx+1))
        else:
            heappop(h)
    return results


def kmergesort(a, k):
    if a == []:
        return a
    else:
        return _mergesort(k)(a)


if __name__ == '__main__':
    import unittest
    from random import randint
    import time

    def random_list(start, stop, size):
        return [randint(start, stop) for _ in xrange(size)]

    class TestKMergesort(unittest.TestCase):

        def test_base_cases(self):
            self.assertEqual(kmergesort([], 4), [])

        def test_returns_sorted_list(self):
            a = random_list(-50, 50, 50)
            sorted_a = sorted(a)
            self.assertEqual(kmergesort(a, 2), sorted_a)
            self.assertEqual(kmergesort(a, 4), sorted_a)
            self.assertEqual(kmergesort(a, 7), sorted_a)
            self.assertEqual(kmergesort(a, 10), sorted_a)

    unittest.main()
