def ksmallest(k, l):
    pass


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
            self.assertEqual(ksmallest(a, 3), sorted(a)[:3])
            b = xrange(100)
            self.assertEqual(ksmallest(b, 10), sorted(b)[:10])

        def test_negative_nums(self):
            a = [-4, 3, 9, -32, 0, -4, 8]
            self.assertEqual(ksmallest(a, 4), sorted(a)[:4])
            b = xrange(-100, 100)
            self.assertEqual(ksmallest(b, 20), sorted(b)[:20])

        def test_instructor_examples(self):
            self.assertEqual(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]), [2, 3, 5, 7])
            self.assertEqual(ksmallest(3, xrange(1000000, 0, -1)), [1, 2, 3])

    unittest.main()
