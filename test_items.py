import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
input1.send_keys(y)
time.sleep(2)

input2 = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
input2.click()
time.sleep(2)

input3 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
input3.click()
time.sleep(2)

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()

# закрываем браузер после всех манипуляций
time.sleep(10)
browser.quit()
