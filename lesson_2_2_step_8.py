import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('S:\\Automation_Py\\python_selenium\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)

base_url = 'http://suninjuly.github.io/file_input.html'
driver.get(base_url)

first_name = driver.find_element(By.XPATH, '//input[@name="firstname"]')
first_name.send_keys('Yan')
last_name = driver.find_element(By.XPATH, '//input[@name="lastname"]')
last_name.send_keys('Surma')
email = driver.find_element(By.XPATH, '//input[@name="email"]')
email.send_keys('test@mail.com')

# Указываем путь к нашему файлу в текущей папке
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

element = driver.find_element(By.XPATH, '//input[@name="file"]')
element.send_keys(file_path)

submit_button = driver.find_element(By.XPATH, ' //button[@type="submit"]')
submit_button.click()


