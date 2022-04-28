from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

try:
    browser.get("http://suninjuly.github.io/selects1.html")
    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")
    a = int(a_element.text)
    b = int(b_element.text)
    c = str(a + b)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()