#https://stepik.org/lesson/228249/step/5?unit=200781
import time
import math
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
driver = webdriver.Chrome()
driver.get("http://SunInJuly.github.io/execute_script.html")

try:
    x = driver.find_element_by_css_selector("#input_value").text
    y = calc(x)
    driver.find_element_by_css_selector("#answer").send_keys(y)
    driver.execute_script("window.scrollBy(0, 150);")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
    driver.find_element_by_css_selector("#answer").send_keys(y)
    driver.find_element_by_css_selector("#robotCheckbox").click()
    driver.find_element_by_css_selector("#robotsRule").click()

finally:
    time.sleep(1000000)
    driver.quit()
