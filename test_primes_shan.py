import unittest
from  code.primes import is_prime

class isPrime(unittest.TestCase):
    def test1(self):
        self.assertTrue(is_prime(5))
    def test2(self):
        self.assertTrue(is_prime(10),"error message shan")

if __name__=='__main__':
    unittest.main()

