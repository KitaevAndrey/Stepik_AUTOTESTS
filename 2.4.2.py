#https://stepik.org/lesson/181384/step/7?unit=156009
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    z = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))#пока цена по price не станет 100
    driver.find_element_by_css_selector("#book").click()
    x = driver.find_element_by_css_selector("#input_value").text
    y = calc(x)
    driver.find_element_by_css_selector("#answer").send_keys(y)
    driver.find_element_by_css_selector("body > form > div > div > button").click()
finally:
    time.sleep(20)
    driver.quit()


