import pr
import unittest


class testfactors(unittest.TestCase):

    def test_facrors(self):
        result = pr.factors(4)
        self.assertEqual(result, [2, 2])


class testisprime(unittest.TestCase):

    def test_is_prime(self):

        result = pr.is_prime(11)
        self.assertEqual(result, True)


class testvowels(unittest.TestCase):

    def test_vowels(self):

        result = pr.vowels("qwrasdeib")
        self.assertEqual(result, ['a', 'e', 'i'])


class testlen(unittest.TestCase):

    def test_len(self):

        result = len("1234567890")
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
