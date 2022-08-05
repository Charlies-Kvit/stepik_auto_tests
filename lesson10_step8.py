from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(5)
    
    button_wait = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID, "input_value").text
    robot_input = browser.find_element(By.ID, "answer")
    robot_input.send_keys(calc(x))
    button = browser.find_element(By.ID, "solve")
    sleep(1)
    button.click()

finally:
    sleep(10)
    browser.quit()
