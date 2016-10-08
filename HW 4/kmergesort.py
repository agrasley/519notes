def kmergesort(a, k):
    pass


if __name__ == '__main__':
    import unittest
    from random import sample
    import time

    class TestKMergesort(unittest.TestCase):

        def test_base_cases(self):
            self.assertEqual(kmergesort([], 4), [])

        def test_returns_sorted_list(self):
            a = sample(xrange(100), 100)
            sorted_a = sorted(a)
            self.assertEqual(kmergesort(a, 2), sorted_a)
            self.assertEqual(kmergesort(a, 4), sorted_a)
            self.assertEqual(kmergesort(a, 10), sorted_a)

        def test_execution_speeds(self):
            a = sample(xrange(500), 500)
            slow_t0 = time.clock()
            kmergesort(a, 4)
            slow_t1 = time.clock() - slow_t0
            medium_t0 = time.clock()
            kmergesort(a, 3)
            medium_t1 = time.clock() - medium_t0
            fast_t0 = time.clock()
            kmergesort(a, 2)
            fast_t1 = time.clock() - fast_t0
            self.assertLess(medium_t1, slow_t1)
            self.assertLess(fast_t1, medium_t1)

    unittest.main()
