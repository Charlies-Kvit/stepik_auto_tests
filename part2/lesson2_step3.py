from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

def sum(a, b):
    sum = int(a) + int(b)
    return str(sum)

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum(a, b))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    sleep(10)
    browser.quit()
