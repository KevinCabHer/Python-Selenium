import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\hecto\OneDrive\Escritorio\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://demo-store.seleniumacademy.com')

    def test_search(self):
        self.assertTrue(self.element_present(By.NAME, 'q'))

    def test_language(self):
        self.assertTrue(self.element_present(By.NAME, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    def element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as var:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)
