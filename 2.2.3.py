#https://stepik.org/lesson/228249/step/7?unit=200781
import time
import math
from selenium import webdriver
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")
try:
    driver.find_element_by_css_selector("body > div > form > div > input:nth-child(2)").send_keys('Андрей')
    driver.find_element_by_css_selector("body > div > form > div > input:nth-child(4)").send_keys('Китаев')
    driver.find_element_by_css_selector("body > div > form > div > input:nth-child(6)").send_keys('kitaevsteam@mail.ru')
    driver.find_element_by_css_selector("#file").send_keys(file_path)
    driver.find_element_by_css_selector("body > div > form > button").click()
finally:
    time.sleep(20)
    driver.quit()