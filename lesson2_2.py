from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    num_element1 = browser.find_element(By.CSS_SELECTOR, "span.nowrap")
    num_element2 = browser.find_element(By.CSS_SELECTOR, "span.nowrap#num2")
    n = int(num_element1.text) + int(num_element2.text)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(n))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
print(n)
