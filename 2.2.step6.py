from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

link = "https://SunInJuly.github.io/execute_script.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)


    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()