from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

try:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    browser.find_element(By.TAG_NAME, "input").send_keys("Boris")
    browser.find_element(By.NAME, "last_name").send_keys("Johnson")
    browser.find_element(By.CLASS_NAME, "city").send_keys("New York")
    browser.find_element(By.ID, "country").send_keys("USA")
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(30)
    browser.quit()
