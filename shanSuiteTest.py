import unittest

from test_sub import SubTest
from test_is_prime import PrimesTestCase

def my_suite():
    suite= unittest.TestSuite() #suite instance
    suite.addTest(unittest.makeSuite(SubTest))#addtest is a keyword
    suite.addTest(unittest.makeSuite(PrimesTestCase))
    runner=unittest.TextTestRunner()
    
    print(runner.run(suite))

my_suite()
