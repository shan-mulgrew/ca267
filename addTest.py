import unittest
from code.add import add

class AddTestShan(unittest.TestCase):

    def test_one(self):
        self.assertEqual(add(2,2),4)
    def test_two(self):
        self.assertEqual(add(1,2),10,"1 +2 !=10")

if __name__ == '__main__':
    unittest.main()
