import unittest
from code.addNum import addNum

class addNumTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(addNum(2,100),102)
    def test_2(self):
        self.assertNotEqual(addNum(5,5),10)

    def test_3(self):
        self.assertNotEqual(addNum(10,10),30)

if __name__ == '__main__':
    unittest.main()

    
