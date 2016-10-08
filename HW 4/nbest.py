def nbesta(a, b):
    pass


def nbestb(a, b):
    pass


def nbestc(a, b):
    pass


if __name__ == '__main__':
    import unittest
    import time
    from random import sample

    class TestNBest(unittest.TestCase):

        def test_base_cases(self):
            self.assertEqual(nbesta([], []), [])
            self.assertEqual(nbestb([], []), [])
            self.assertEqual(nbestc([], []), [])
            self.assertIs(nbesta([1], []), None)
            self.assertIs(nbestb([1], []), None)
            self.assertIs(nbestc([1], []), None)

        def test_random_lists(self):
            a = sample(xrange(-15, 15), 25)
            b = sample(xrange(-5, 20), 25)
            self.assertEqual(nbesta(a, b), nbestb(a, b))
            self.assertEqual(nbestb(a, b), nbestc(a, b))

        def test_instructor_examples(self):
            a, b = [4, 1, 5, 3], [2, 6, 3, 4]
            result = [(1, 2), (1, 3), (3, 2), (1, 4)]
            self.assertEqual(nbesta(a, b), result)
            self.assertEqual(nbestb(a, b), result)
            self.assertEqual(nbestc(a, b), result)

        def test_execution_speeds(self):
            a = sample(xrange(25), 25)
            b = sample(xrange(25), 25)
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
