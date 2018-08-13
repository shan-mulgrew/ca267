import unittest
from test_add import AddTestCase
from test_is_prime import PrimesTestCase

def my_suite():
    suite= unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AddTestCase))
    suite.addTest(unittest.makeSuite(PrimesTestCase))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
    
    

