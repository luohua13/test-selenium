import HtmlTestRunner
import unittest
from selenium impoer webdriver

class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_sample(self):
        browser = webdriver.Chrome()
        print("cooooooooooool")
        browser.get("http://www.baidu.com")
        browser.find_element_by_id("kw").send_keys("selenium")
        browser.find_element_by_id("su").click()
        browser.quit()
 
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="test-report", add_timestamp=False))
