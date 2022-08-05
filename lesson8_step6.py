from operator import imod
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element(By.ID, "input_value").text
    robot_input = browser.find_element(By.ID, "answer")
    robot_input.send_keys(calc(x))
    browser.execute_script("window.scrollBy(0, 100);")
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_radiobutton = browser.find_element(By.ID, "robotsRule")
    robot_checkbox.click()
    robot_radiobutton.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(10)
    browser.quit()
