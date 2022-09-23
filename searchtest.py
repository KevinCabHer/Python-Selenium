import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\hecto\OneDrive\Escritorio\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://demo-store.seleniumacademy.com')

    def test_sear_tee(self):
        driver = self.driver
        search = driver.find_element(By.NAME, 'q')
        search.clear()
        search.send_keys('tee')
        search.submit()

    def test_search_shaker(self):
        driver = self.driver
        search = driver.find_element(By.NAME, 'q')
        search.clear()
        search.send_keys('salt shaker')
        search.submit()

        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
