from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

try:
    #Заполняем форму
    browser.get("http://suninjuly.github.io/registration1.html")
    first_name = browser.find_element(By.CSS_SELECTOR, "input.first:required")
    first_name.send_keys("John")
    last_name = browser.find_element(By.CSS_SELECTOR, "input.second:required")
    last_name.send_keys("Doe")
    email = browser.find_element(By.CSS_SELECTOR, "input.third:required")
    email.send_keys("johndoe@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()