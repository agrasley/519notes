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


@memoize
def bsts(n):
    if n == 0:
        return 1
    else:
        i = 0
        total = 0
        while i < n/2:
            total += 2 * bsts(i) * bsts(n - 1 - i)
            i += 1
        if n % 2 == 1:
            total += bsts(i) * bsts(n - 1 - i)
        return total


if __name__ == '__main__':
    import unittest

    class TestBsts(unittest.TestCase):

        def test_instructor_examples(self):
            self.assertEqual(bsts(3), 5)
            self.assertEqual(bsts(5), 42)

    unittest.main()
