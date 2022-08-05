from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    img = browser.find_element(By.TAG_NAME, "img")
    x = img.get_attribute("valuex")
    robo_input = browser.find_element(By.ID, "answer")
    robo_input.send_keys(calc(x))
    robo_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robo_checkbox.click()
    robo_radiobutton = browser.find_element(By.ID, "robotsRule")
    robo_radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(10)
    browser.quit()
