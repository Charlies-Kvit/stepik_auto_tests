from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])
    
    sleep(1)

    x = browser.find_element(By.ID, "input_value").text
    robot_input = browser.find_element(By.TAG_NAME, "input")
    robot_input.send_keys(calc(x))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(10)
    browser.quit()
