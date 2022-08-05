from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    browser = webdriver.Chrome()
    browser.get("https://web.telegram.org/k/")
    sleep(5)

    button = browser.find_element(By.CLASS_NAME, "c-ripple")
    button.click()

    sleep(5)

    phone_input = browser.find_element(By.CLASS_NAME, "input-field-phone .input-field-input")
    phone_input.send_keys("9852120170")
    button = browser.find_element(By.XPATH, '//span[text() = "Next"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    sleep(5)
    button.click()


finally:
    sleep(10)
    browser.quit()
