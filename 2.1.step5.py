from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()