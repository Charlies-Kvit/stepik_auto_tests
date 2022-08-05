from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    robo_input = browser.find_element(By.ID, "answer")
    robo_input.send_keys(calc(x))
    robo_checkbox = browser.find_element(By.CSS_SELECTOR, '[for = "robotCheckbox"]')
    robo_checkbox.click()
    robo_radiobutton = browser.find_element(By.CSS_SELECTOR, '[for = "robotsRule"]')
    robo_radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()