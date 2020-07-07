#https://stepik.org/lesson/165493/step/6?unit=140087
import time
import math
from selenium import webdriver
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")
try:
      x= driver.find_element_by_css_selector("#treasure")
      a= x.get_attribute("valuex")
      y=calc(a)
      driver.find_element_by_css_selector("#answer").send_keys(y)
      driver.find_element_by_css_selector("#robotCheckbox").click()
      driver.find_element_by_css_selector("#robotsRule").click()
      driver.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(10)
    driver.quit()