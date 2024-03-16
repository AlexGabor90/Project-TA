"""
In this file you may find the report creating data.
"""
import unittest
import HtmlTestRunner
from Tests.Function_Test_01 import TestSite
from Tests.Function_Test_02 import TestTitle
from Tests.Function_Test_03 import TestProduct
from Tests.Function_Test_04 import TestLowProduct
from Tests.Function_Test_05 import TestHighProduct
from Tests.Function_Test_06 import UnlistedProduct
from Tests.Function_Test_07 import LoginURL
from Tests.Function_Test_08 import LoginErrorMsg
from Tests.Function_Test_09 import TestLoginFail
from Tests.Function_Test_10 import TestLogin


class TestingSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestSite),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestTitle),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestLowProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestHighProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(UnlistedProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(LoginURL),
                             unittest.defaultTestLoader.loadTestsFromTestCase(LoginErrorMsg),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginFail),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Result Test Elefant.ro',
            report_title='Result Test Elefant.ro product and login'
        )

        runner.run(test_suite)