from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class TestRegistration(unittest.TestCase):
    def test1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CLASS_NAME, "first_block .first")
        input2 = browser.find_element(By.CLASS_NAME, "first_block .second")
        input3 = browser.find_element(By.CLASS_NAME, "first_block .third")
        input1.send_keys("Gleb")
        input2.send_keys("Butovich")
        input3.send_keys("g@mail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button")
        sleep(5)
        button.click()
        sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "ERROR ON THIS PAGE: http://suninjuly.github.io/registration1.html")
        browser.quit()

    def test2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CLASS_NAME, "first_block .first")
        input2 = browser.find_element(By.CLASS_NAME, "first_block .second")
        input3 = browser.find_element(By.CLASS_NAME, "first_block .third")
        input1.send_keys("Gleb")
        input2.send_keys("Butovich")
        input3.send_keys("g@mail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button")
        sleep(5)
        button.click()
        sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "ERROR ON THIS PAGE: http://suninjuly.github.io/registration2.html")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
