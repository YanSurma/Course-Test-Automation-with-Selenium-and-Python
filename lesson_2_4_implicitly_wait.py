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

driver.implicitly_wait(5)
driver.get("http://suninjuly.github.io/cats.html")

button = driver.find_element(By.ID, "verify")
button.click()
message = driver.find_element(By.ID, "verify_message")

assert "successful" in message.text
