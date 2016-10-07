from bisect import bisect


def find(a, x, k):
    len_a = len(a)
    if k > len_a or k <= 0:
        return None
    elif k == len_a:
        return a
    else:
        p2 = bisect(a, x)
        p1 = p2 - 1
        i = 0
        while i < k:
            if p1 < 0:
                p2 += 1
            elif p2 >= len_a:
                p1 -= 1
            else:
                elt1 = a[p1]
                elt2 = a[p2]
                distance1 = abs(x - elt1)
                distance2 = abs(x - elt2)
                if distance1 <= distance2:
                    p1 -= 1
                else:
                    p2 += 1
            i += 1
        return a[(p1 + 1):p2]


if __name__ == '__main__':
    import unittest
    from closest_unsorted import find as unsorted_find
    import time

    class TestClosestSorted(unittest.TestCase):

        def test_k_gt_len(self):
            self.assertIs(find([1, 2], 0, 3), None)

        def test_instructor_results(self):
            self.assertEqual(find([1, 2, 3, 4, 4, 6, 6], 5, 3), [4, 4, 6])
            self.assertEqual(find([1, 2, 3, 4, 4, 5, 6], 4, 5), [2, 3, 4, 4, 5])

        def test_never_use_right_ptr(self):
            self.assertEqual(find([2, 2, 2, 5], 3, 3), [2, 2, 2])

        def test_never_use_left_ptr(self):
            self.assertEqual(find([2, 5, 5, 5], 4, 3), [5, 5, 5])

        def test_k_gt_each_elt(self):
            self.assertEqual(find([1, 2, 3, 4, 5], 6, 3), [3, 4, 5])

        def test_k_lt_each_elt(self):
            self.assertEqual(find([1, 2, 3, 4, 5], 0, 2), [1, 2])

        def test_versus_unsorted(self):
            a = range(1000)
            self.assertEqual(find(a, 800, 100), unsorted_find(a, 800, 100))
            unsorted_t0 = time.clock()
            unsorted_find(a, 800, 100)
            unsorted_t1 = time.clock() - unsorted_t0
            faster_t0 = time.clock()
            find(a, 800, 100)
            faster_t1 = time.clock() - faster_t0
            self.assertLess(faster_t1, unsorted_t1)
            print "\nfaster_t1: "
            print faster_t1
            print "\nunsorted_t1: "
            print unsorted_t1
            print "\n"

    unittest.main()
