#https://stepik.org/lesson/181384/step/5?unit=156009
import time
import math
from selenium import webdriver
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/cats.html")
driver.implicitly_wait(5)

try:
    driver.find_element_by_id("button")
finally:
    time.sleep(20)
    driver.quit()