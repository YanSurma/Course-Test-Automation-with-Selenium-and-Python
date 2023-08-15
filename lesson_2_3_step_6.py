import math
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('S:\\Automation_Py\\python_selenium\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)

base_url = 'http://suninjuly.github.io/redirect_accept.html'
driver.get(base_url)

trollface_button = driver.find_element(By.XPATH, '//button[@class="trollface btn btn-primary"]')
trollface_button.click()

# Обьявляем метод window_handles для перехода по вкладкам браузера
new_window = driver.window_handles[1]
first_window = driver.window_handles[0]

# Открываем новую вкладку
driver.switch_to.window(new_window)

# Получаем x и производим вычисление
value = driver.find_element(By.XPATH, '//span[@id="input_value"]')
x = int(value.text)
result = math.log(abs(12 * math.sin(x)))

text = driver.find_element(By.XPATH, '//input[@name="text"]')
text.send_keys(result)

# Отправляем рез-т
submit_button = driver.find_element(By.XPATH, ' //button[@type="submit"]')
submit_button.click()
