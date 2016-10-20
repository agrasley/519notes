from heapq import heapify, heapreplace


def _sort_heap(h, length):
    if length == 1:
        h[0] = -h[0]
        return h
    else:
        x = h[0]
        h[0] = h[length - 1]
        h[length - 1] = -x
        _bubble_down(h, 0, length - 1)
        return _sort_heap(h, length - 1)


def _bubble_down(h, i, length):
    if length > 2*i+1:
        if 2*i+2 >= length or h[2*i+1] <= h[2*i+2]:
            if h[i] > h[2*i+1]:
                x = h[i]
                h[i] = h[2*i+1]
                h[2*i+1] = x
                _bubble_down(h, 2*i+1, length)
            else:
                return
        else:
            if h[i] > h[2*i+2]:
                x = h[i]
                h[i] = h[2*i+2]
                h[2*i+2] = x
                _bubble_down(h, 2*i+2, length)
            else:
                return
    else:
        return


def _modify_heap(h, x):
    if x <= h[0]:
        return
    else:
        heapreplace(h, x)


def ksmallest(k, l):
    if k > len(l):
        return None
    else:
        heap = []
        i = 0
        while i < k:
            heap.append(-l[i])
            i += 1
        heapify(heap)
        while i < len(l):
            _modify_heap(heap, -l[i])
            i += 1
        return _sort_heap(heap, k)


if __name__ == '__main__':
    import unittest

    class TestDataStream(unittest.TestCase):

        def test_base_cases(self):
            self.assertIs(ksmallest(3, [1, 2]), None)
            self.assertIs(ksmallest(5, xrange(3)), None)

        def test_returns_k_elts(self):
            self.assertEqual(len(ksmallest(2, [1, 2, 3])), 2)
            self.assertEqual(len(ksmallest(5, xrange(100))), 5)

        def test_returns_sorted_list(self):
            a = [7, 8, 1, 4, 0, -4, 69]
            self.assertEqual(ksmallest(3, a), sorted(a)[:3])
            b = xrange(100)
            self.assertEqual(ksmallest(10, b), sorted(b)[:10])

        def test_negative_nums(self):
            a = [-4, 3, 9, -32, 0, -4, 8]
            self.assertEqual(ksmallest(4, a), sorted(a)[:4])
            b = xrange(-100, 100)
            self.assertEqual(ksmallest(20, b), sorted(b)[:20])

        def test_instructor_examples(self):
            self.assertEqual(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]), [2, 3, 5, 7])
            self.assertEqual(ksmallest(3, xrange(1000000, 0, -1)), [1, 2, 3])

    unittest.main()
