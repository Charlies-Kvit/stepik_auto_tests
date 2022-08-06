import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('site', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test(browser, site):
    browser.implicitly_wait(10)
    browser.get(site)
    robo_input = browser.find_element(By.TAG_NAME, "textarea")
    robo_input.send_keys(math.log(int(time.time())))
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    total = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert total == "Correct!", f"expected: Correct! found: {total}"

