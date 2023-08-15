from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import math
import os


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('S:\\Automation_Py\\python_selenium\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
driver.maximize_window()

driver.get('http://suninjuly.github.io/explicit_wait2.html')

wait = WebDriverWait(driver, 12)
price = wait.until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), "100"))

if price:
    book_button = driver.find_element(By.XPATH, '//button[@id="book"]')
    book_button.click()

# Получаем x и производим вычисление
value = driver.find_element(By.XPATH, '//span[@id="input_value"]')
x = int(value.text)
result = math.log(abs(12 * math.sin(x)))

text = driver.find_element(By.XPATH, '//input[@name="text"]')
text.send_keys(result)

# Отправляем рез-т
submit_button = driver.find_element(By.XPATH, ' //button[@id="solve"]')
submit_button.click()

