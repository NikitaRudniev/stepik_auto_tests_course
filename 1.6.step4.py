from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Boris")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Johnson")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("New York")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("USA")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
