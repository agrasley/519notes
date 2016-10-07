from random import randint


def _naive_implementation(a):  # only for testing
    len_a = len(a)
    z = 0
    results = []
    while z < len_a:
        x = 0
        while x < len_a:
            if x != z:
                y = x + 1
                while y < len_a:
                    if y != z and a[x] + a[y] == a[z]:
                        results.append((a[x], a[y], a[z]))
                    y += 1
            x += 1
        z += 1
    return results


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


def _two_pointers(a, c, i, j, k, results):
    if j == k:
        return
    elif i == j:
        return _two_pointers(a, c, i, j+1, k, results)
    elif i == k:
        return _two_pointers(a, c, i, j, k-1, results)
    elif a[j] + a[k] == c:
        results.append((a[j], a[k], c))
        if k - j == 1:
            return
        else:
            return _two_pointers(a, c, i, j+1, k-1, results)
    elif a[j] + a[k] > c:
        return _two_pointers(a, c, i, j, k-1, results)
    else:
        return _two_pointers(a, c, i, j+1, k, results)


def find(a):
    len_a = len(a)
    if len_a < 3:
        return None
    sorted_a = _qsort(a)
    results = []
    for i in range(len_a):
        c = sorted_a[i]
        j = 0
        k = len_a - 1
        _two_pointers(sorted_a, c, i, j, k, results)
    return results


if __name__ == '__main__':
    import unittest
    import time

    class TestXYZ(unittest.TestCase):

        def test_lt_three_elts(self):
            self.assertIs(find([1, 2]), None)

        def test_instructor_results(self):
            self.assertEqual(find([1, 4, 2, 3, 5]), [(1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)])

        def test_no_sums(self):
            self.assertEqual(find([1, 2, 4]), [])

        def test_jeff_tests(self):
            self.assertEqual(find([11, 4, 2, 3, 5, 7]), [(2, 3, 5), (2, 5, 7), (3, 4, 7), (4, 7, 11)])
            self.assertEqual(find([1, 2, 3, 5]), [(1, 2, 3), (2, 3, 5)])

        def test_versus_naive(self):
            a = range(50)
            self.assertEqual(len(find(a)), len(_naive_implementation(a)))
            naive_t0 = time.clock()
            _naive_implementation(a)
            naive_t1 = time.clock() - naive_t0
            faster_t0 = time.clock()
            find(a)
            faster_t1 = time.clock() - faster_t0
            self.assertLess(faster_t1, naive_t1)
            print "\nfaster_t1: "
            print faster_t1
            print "\nnaive_t1: "
            print naive_t1
            print "\n"

    unittest.main()
