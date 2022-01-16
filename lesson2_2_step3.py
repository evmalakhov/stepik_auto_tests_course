from selenium import webdriver
import time 
import math

from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)


    x1_element = browser.find_element_by_id("num1").text
    x2_element = browser.find_element_by_id("num2").text
    x1 = int(x1_element)
    x2 = int(x2_element)
    y = x1 + x2

    print("x1: ", x1_element);
    print("x2: ", x2_element);

    print("x1: ", x1);
    print("x2: ", x2);

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(y))


    time.sleep(0.5)

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()


finally:
    time.sleep(30)
    browser.quit()


