import unittest
 
from test_sub import SubTest
 
 
def my_suite():
    suite = unittest.TestSuite() #instance of Testsuite
    result = unittest.TestResult()#instance of Testresult
    suite.addTest(unittest.makeSuite(SubTest))# addTest is a keyword
    #SubTest class contains unittest in file "test_sub.py" to test my implementation 
	#of substraction in    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
 
my_suite()
