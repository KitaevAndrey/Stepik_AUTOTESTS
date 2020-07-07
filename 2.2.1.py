#https://stepik.org/lesson/228249/step/2?unit=200781
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects1.html")
try:
    x = driver.find_element_by_css_selector("#num1").text
    y = driver.find_element_by_css_selector("#num2").text
    z = str(int(x) + int(y))
    print(x,y,z)
    select = Select(driver.find_element_by_tag_name("select"))#https://stepik.org/lesson/228249/step/2?unit=200781
    select.select_by_value(z)
    driver.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(10)
    driver.quit()