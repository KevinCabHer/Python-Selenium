import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class hello_word(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\hecto\OneDrive\Escritorio\Selenium\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_word(self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='hello_word_report'))