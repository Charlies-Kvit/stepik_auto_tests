from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    input1 = browser.find_element(By.NAME, "firstname")
    input2 = browser.find_element(By.NAME, "lastname")
    input3 = browser.find_element(By.NAME, "email")
    input1.send_keys("Gleb")
    input2.send_keys("Butovich")
    input3.send_keys("g@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(10)
    browser.quit()
