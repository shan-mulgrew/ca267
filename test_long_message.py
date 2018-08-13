import unittest

class LongMessageTestcase(unittest.TestCase):

    def test_use_long_message(self):
        # long message is the mechanism for printing a custom message
        actual_values = 4
        expected_values = 5
        self.assertNotEqual(4, 5, "two numbers are not equal")

if __name__ == '__main__':
    unittest.main()
