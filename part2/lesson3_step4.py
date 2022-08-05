from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    robot_input = browser.find_element(By.ID, "answer")
    robot_input.send_keys(calc(x))
    sleep(1)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(10)
    browser.quit()
