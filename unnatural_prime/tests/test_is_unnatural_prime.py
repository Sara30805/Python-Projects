import unittest
from is_unnatural_prime import is_unnatural_prime

class TestUnnaturalPrime(unittest.TestCase):

    def test_primes(self):
        primes = [19, -23, 97, -61]
        for n in primes:
            with self.subTest(n=n):
                self.assertTrue(is_unnatural_prime(n))

    def test_not_primes(self):
        non_primes = [0, 1, -1, 99, -44]
        for n in non_primes:
            with self.subTest(n=n):
                self.assertFalse(is_unnatural_prime(n))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            is_unnatural_prime(3.5)




if __name__ == "__main__":
    unittest.main()
