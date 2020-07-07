#https://stepik.org/lesson/184253/step/2?unit=158843
import time
import math
from selenium import webdriver
import os
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/alert_accept.html")
try:
    driver.find_element_by_css_selector("body > form > div > div > button").click()
    alert = driver.switch_to.alert
    alert.accept()
    x = driver.find_element_by_css_selector("#input_value").text
    y = calc(x)
    driver.find_element_by_css_selector("#answer").send_keys(y)
    driver.find_element_by_css_selector("body > form > div > div > button").click()
finally:
    time.sleep(20)
    driver.quit()