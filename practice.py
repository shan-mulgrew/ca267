import unittest
from code.sub import sub

class practiceTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual(sub(3,2),1)
    def test_two(self):
        self.assertNotEqual(sub(5,3),1)
if __name__== "__main__":
    unittest.main()
