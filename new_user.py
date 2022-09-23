import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class NewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\hecto\OneDrive\Escritorio\Python-Selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")
        driver.implicitly_wait(10)

    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[5]/div/ul/li[6]/a').click()
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span').click()
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')

        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        news_letter_subscription = driver.find_element(By.ID, 'is_subscribed')
        submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and submit.is_enabled())

        first_name.send_keys('Prueba 1')
        middle_name.send_keys('prueba 1')
        last_name.send_keys('prueba 1')
        email_address.send_keys('prueba 1')
        password.send_keys('ABCdef12345')
        confirm_password.send_keys('ABCdef12345')
        driver.implicitly_wait(20)
        submit.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)