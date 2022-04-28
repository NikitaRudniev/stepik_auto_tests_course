from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("John")
    browser.find_element(By.NAME, "lastname").send_keys("Doe")
    browser.find_element(By.NAME, "email").send_keys("johndoe@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(10)
    browser.quit()
