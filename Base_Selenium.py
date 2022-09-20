# SELECTORES

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\hecto\OneDrive\Escritorio\Selenium\chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com")
        driver.implicitly_wait(1)

    def test_search_id(self):
        sear_field = self.driver.find_element(By.ID, "search")
    
    def test_search_class(self):
        sear_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_name(self):
        sear_field = self.driver.find_element(By.NAME, "q")
    def tearDown(self):
        self.driver.quit()

    
if __name__ == "__main__":
    unittest.main(verbosity=2)


'''
En su lugar, tienes que usar find_element(). Como ejemplo:

Tienes que incluir las siguientes importaciones

from selenium.webdriver.common.by import By
usando class_name:

button = driver.find_element_by_class_name("quiz_button")
Necesita ser reemplazado con:

button = driver.find_element(By.CLASS_NAME, "quiz_button")
En líneas similares también hay que cambiar lo siguiente:

usando id:

element = find_element_by_id("element_id")
Necesita ser reemplazado con:

element = driver.find_element(By.ID, "element_id")
usando name:

element = find_element_by_name("element_name")
Necesita ser reemplazado con:

element = driver.find_element(By.NAME, "element_name")
usando link_text:

element = find_element_by_link_text("element_link_text")
Necesita ser reemplazado con:

element = driver.find_element(By.LINK_TEXT, "element_link_text")
usando partial_link_text:

element = find_element_by_partial_link_text("element_partial_link_text")
Necesita ser reemplazado con:

element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
usando tag_name:

element = find_element_by_tag_name("element_tag_name")
Necesita ser reemplazado con:

element = driver.find_element(By.TAG_NAME, "element_tag_name")
usando css_selector:

element = find_element_by_css_selector("element_css_selector")
Necesita ser reemplazado con:

element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")
usando xpath:

element = find_element_by_xpath("element_xpath")
Necesita ser reemplazado con:

element = driver.find_element(By.XPATH, "element_xpath")
'''