from random import randint, sample


def _selection_sort(a, i):  # just for the naive implementation
    min_idx = i
    j = i + 1
    while j < len(a):
        if a[min_idx] > a[j]:
            min_idx = j
        j += 1
    i_elt = a[i]
    a[i] = a[min_idx]
    a[min_idx] = i_elt


def _naive_implementation(a, x, k):  # just for testing
    distances = [abs(y - x) for y in a]
    distances_copy = distances[:]
    i = 0
    while i < k:
        _selection_sort(distances_copy, i)
        i += 1
    selection = distances_copy[k-1]
    result = []
    lt = 0
    for q in distances:
        if q < selection:
            lt += 1
    num_eq = k - lt
    i = 0
    while i < len(a):
        if distances[i] < selection:
            result.append(a[i])
        elif distances[i] == selection and num_eq > 0:
            result.append(a[i])
            num_eq -= 1
        if len(result) == k:
            return result
        i += 1


def _qsort(a):  # just for testing
    if a == []:
        return []
    else:
        pindex = randint(0, len(a)-1)
        a[0], a[pindex] = a[pindex], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return _qsort(left) + [pivot] + _qsort(right)


def _less_naive(a, x, k):  # just for testing
    distances = [abs(y - x) for y in a]
    sorted_distances = _qsort(distances[:])
    selection = sorted_distances[k-1]
    result = []
    lt = 0
    for q in distances:
        if q < selection:
            lt += 1
    num_eq = k - lt
    i = 0
    while i < len(a):
        if distances[i] < selection:
            result.append(a[i])
        elif distances[i] == selection and num_eq > 0:
            result.append(a[i])
            num_eq -= 1
        if len(result) == k:
            return result
        i += 1


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


def find(a, x, k):
    len_a = len(a)
    if k > len_a or k <= 0:
        return None
    elif k == len_a:
        return a
    else:
        distances = [abs(y - x) for y in a]
        selection = _qselect(k, distances[:])
        result = []
        lt = 0
        for q in distances:
            if q < selection:
                lt += 1
        num_eq = k - lt
        i = 0
        while i < len_a:
            if distances[i] < selection:
                result.append(a[i])
            elif distances[i] == selection and num_eq > 0:
                result.append(a[i])
                num_eq -= 1
            if len(result) == k:
                return result
            i += 1


if __name__ == '__main__':
    import unittest
    import time

    class TestClosestUnsorted(unittest.TestCase):

        def test_k_gt_len(self):
            self.assertIs(find([1, 2], 1.5, 3), None)

        def test_returns_elts_in_order(self):
            self.assertEqual(find([1, 2, 1, 2, 1], 1.5, 4), [1, 2, 1, 2])

        def test_returns_lt_before_eq_duplicates(self):
            self.assertEqual(find([2, 2, 2, 2, 2, 1], 1, 3), [2, 2, 1])

        def test_k_gt_each_elt(self):
            self.assertEqual(find([1, 2, 3, 4, 5], 6, 3), [3, 4, 5])

        def test_k_lt_each_elt(self):
            self.assertEqual(find([1, 2, 3, 4, 5], 0, 2), [1, 2])

        def test_mult_duplicates(self):
            self.assertEqual(find([1, 2, 2, 1, 2, 1, 2, 2], 1.2, 5), [1, 2, 2, 1, 1])

        def test_instructor_results(self):
            self.assertEqual(find([4, 1, 3, 2, 7, 4], 5.2, 2), [4, 4])
            self.assertEqual(find([4, 1, 3, 2, 7, 4], 6.5, 3), [4, 7, 4])

        def test_versus_naive(self):
            a = sample(xrange(1000), 1000)
            self.assertEqual(find(a, 800, 100), _naive_implementation(a, 800, 100))
            naive_t0 = time.clock()
            _naive_implementation(a, 800, 100)
            naive_t1 = time.clock() - naive_t0
            faster_t0 = time.clock()
            find(a, 800, 100)
            faster_t1 = time.clock() - faster_t0
            self.assertLess(faster_t1, naive_t1)
            print "\nfaster_t1: "
            print faster_t1
            print "\nnaive_t1: "
            print naive_t1
            print "\n"

        def test_versus_less_naive(self):
            a = sample(xrange(1000), 1000)
            self.assertEqual(find(a, 800, 100), _less_naive(a, 800, 100))
            less_naive_t0 = time.clock()
            _less_naive(a, 800, 100)
            less_naive_t1 = time.clock() - less_naive_t0
            faster_t0 = time.clock()
            find(a, 800, 100)
            faster_t1 = time.clock() - faster_t0
            self.assertLess(faster_t1, less_naive_t1)
            print "\nfaster_t1: "
            print faster_t1
            print "\nless_naive_t1: "
            print less_naive_t1
            print "\n"

    unittest.main()
